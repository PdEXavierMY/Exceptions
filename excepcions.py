import re
from introducir import solicitar_introducir_cadena

def cuenta_electronica():
    correo = solicitar_introducir_cadena("Introduzca su correo")
    print(comprobar(correo))

def comprobar(correo):