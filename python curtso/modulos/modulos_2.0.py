# si el modulo estuviera dentro de una carpeta en la misma ruta
#import funciones_creadas.saludar as saludo
import sys
sys.path.append("C:\\Users\\felip\\OneDrive\\Escritorio\\python curtso\\funciones_creadas")

import funcion_crear_dict_con_nombre_apellido as funci

sali = funci.saludar()
print(sali)
