import re
from introducir import solicitar_introducir_cadena

def cuenta_electronica():
    correo = solicitar_introducir_cadena("Introduzca su correo")
    if comprobar(correo) == False:
        print("Direccion no válida. Por favor introduzca un correo del formato xxx@xxx.xxx")
        cuenta_electronica()
    else:
        usuario = []
        nombre = correo.split("@")
        usuario.append(nombre[0])
        print(usuario)

def comprobar(correo):
    escorreo = re.search(".*@.*\..*", correo)
    if escorreo == None:
        return False
    else:
        return True

cuenta_electronica()