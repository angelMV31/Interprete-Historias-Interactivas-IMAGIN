import sys
from interpreter import ImaginInterpreter

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py ../stories/tu_historia.imx")
        return

    archivo_ruta = sys.argv[1]
    
    try:
        with open(archivo_ruta, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
        
        app = ImaginInterpreter()
        app.cargar_historia(lineas)
        print("--- BIENVENIDO A IMAGIN ---")
        app.ejecutar(lineas)
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo_ruta}")

if __name__ == "__main__":
    main()