from posixpath import split
import re
from introducir.cadena import solicitar_introducir_cadena, solicitar_introducir_palabra

def comprobar(texto):
    if re.search("*.@.*\..*", texto) == None:
        print("Introduzca un correo válido!!")
        usuario()
    else:
        return True

def usuario():
    correo = solicitar_introducir_palabra("Introduzca su correo")
    if comprobar(correo) == True:
        separado = split("@")
        print(separado)

x = re.search("*.@.*\..*", "javi@gmail.com")
print(x)