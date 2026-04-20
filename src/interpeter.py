import re

class ImaginXInterpreter:
    def __init__(self):
        self.variables = {}
        self.escena_actual = "inicio"

    def ejecutar_linea(self, linea):
        # Ejemplo muy básico de procesamiento con Regex
        if linea.startswith("SET"):
            # Lógica para SET variable = valor
            match = re.match(r"SET (\w+) = (\w+)", linea)
            if match:
                var, val = match.groups()
                self.variables[var] = val
            else:
                print("Error: Sintaxis de SET incorrecta") # Basado en tus ejemplos de error

        elif "GOTO" in linea:
            # Lógica para FROM escena GOTO destino
            partes = linea.split()
            self.escena_actual = partes[3] 
            print(f"Cambiando a escena: {self.escena_actual}")

# Uso inicial
interprete = ImaginXInterpreter()
interprete.ejecutar_linea("FROM inicio GOTO pasillo_oscuro")