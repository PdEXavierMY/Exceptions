import re
from introducir import solicitar_introducir_cadena

class correo_electronico:
    def cuenta_electronica():
        correo = solicitar_introducir_cadena("Introduzca su correo")
        comprobacion = correo_electronico.comprobar(correo)
        if comprobacion == False:
            print("Direccion no válida. Por favor introduzca un correo del formato xxx@xxx.xxx")
            correo_electronico.cuenta_electronica()
        else:
            if comprobacion == 1:
                usuario = []
                nombre = correo.split("@")
                usuario.append(nombre[0])
                print("¡Bienvenido "+str(usuario[0])+"!")
            elif comprobacion == 2:
                print("Extensión no reconocida, solo se admite '.com' o '.es'\nCuenta bloqueada a causa de un posible ataque.")
                exit()

    def comprobar(correo):
        escorreo = re.search(".*@.*\..*", correo)
        if escorreo == None:
            return False
        else:
            escorreo1 = re.search(".com$", correo)
            escorreo2 = re.search(".es$", correo)
            if escorreo1 or escorreo2 != None:
                return 1
            else:
                return 2