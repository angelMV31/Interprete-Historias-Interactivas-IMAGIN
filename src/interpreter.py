import re

class ImaginInterpreter:
    def __init__(self):
        self.variables = {}
        self.escenas = {}
        self.escena_actual = None
        self.finalizado = False

    def cargar_historia(self, lineas):
        """Mapea dónde comienza cada escena en el archivo."""
        for i, linea in enumerate(lineas):
            linea = linea.strip()
            if linea.startswith("FROM"):
                match = re.match(r"FROM\s+(\w+)", linea)
                if match:
                    nombre = match.group(1)
                    if self.escena_actual is None:
                        self.escena_actual = nombre
                    self.escenas[nombre] = i

    def ejecutar(self, lineas):
        """Ciclo principal de ejecución."""
        while not self.finalizado and self.escena_actual in self.escenas:
            indice = self.escenas[self.escena_actual]
            for i in range(indice, len(lineas)):
                linea = lineas[i].strip()
                if not linea: continue

                #lógica de comandos
                if self.procesar_linea(linea):
                    break

    def procesar_linea(self, linea):
        #error de escritura: FORM en lugar de FROM
        if "FORM" in linea:
            print("\nError: palabra clave mal escrita (FORM en lugar de FROM)")
            self.finalizado = True
            return True

        #comando: FROM ... GOTO
        if "GOTO" in linea and "FROM" in linea:
            match = re.match(r"FROM\s+(\w+)\s+GOTO\s+(\w+)", linea)
            if match:
                self.escena_actual = match.group(2)
                return True

        #comando: SET (con validación de =)
        elif linea.startswith("SET"):
            if "=" not in linea:
                print(f"\nError en '{linea}': falta operador =")
                self.finalizado = True
                return True
            match = re.match(r"SET\s+(\w+)\s+=\s+(.*)", linea)
            if match:
                var, val = match.groups()
                self.variables[var] = self.variables.get(val, val)
            return False

        #comando: READANSWER
        elif linea.startswith("READANSWER"):
            var_name = linea.split()[1]
            self.variables[var_name] = input("> ")
            return False

        #comando: OPTION
        elif linea.startswith("OPTION"):
            opciones_str = re.search(r"\((.*)\)", linea).group(1)
            opciones = [o.strip() for o in opciones_str.split(",")]
            print("\nOpciones:")
            for idx, opt in enumerate(opciones, 1):
                print(f"{idx}. {opt}")
            input("\nSelecciona una opción para continuar...")
            return False

        #finales
        elif linea.startswith("DISPLAYEND"):
            print(f"\nFIN: {linea.replace('DISPLAYEND ', '')}")
            self.finalizado = True
            return True
        
        elif linea.startswith("DISPLAYERROR"):
            print(f"\nERROR DEL SISTEMA: {linea.replace('DISPLAYERROR ', '')}")
            self.finalizado = True
            return True

        return False