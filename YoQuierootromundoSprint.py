# Elaborar un programa que recorra una lista con los nombres de 10 de sus futuros usuarios de tu
# aplicación (pueden ser personas, pacientes, organizaciones sociales o instituciones públicas).
# Mediante una función, a todos los usuarios se les creará una cuenta automáticamente.
# Asigne una contraseña para cada cuenta. La contraseña debe ser creada con random y debe
# cumplir con los siguientes criterios: mayúsculas, minúsculas y números.
# Cada cuenta debe guardarse en una nueva variable con su respectiva contraseña.
# Por cada cuenta debe pedir un número telefónico para contactarse.

# El programa no terminará de preguntar por los números hasta que todas las organizaciones
# tengan un número de contacto asignado.
# El programa debe verificar que el número telefónico tenga 8 dígitos numéricos.
# Se debe guardar como un string.

import random

def crear_cuenta():
    usuarioslist = ["xabi", "alan", "juan", "pedro","roberto", "maria", "teresa", "veronica", "daniela", "carmen"]
    for usuario in usuarioslist:
        usuarios[usuario]=[]

def crear_password():
    letrasMin ="abcdefghijklmnopqrstuvwxyz"
    LetasMay= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    unir = f"{letrasMin}{LetasMay}{numeros}"
    longitud = 10
    extension = random.sample(unir,longitud)
    contrasena = "" .join(extension)
    return contrasena

def crear_fono(user):
    print(f"A continuacion debe ingresar un fono para de 8 digitos numericos")
    fono=int(input(f"ingresar fono asignado para {user}: "))
    verificador_fono=str(fono)
    if len(verificador_fono) == 8:
        print("Fono registrado")
        return fono
    else:
        print("!!EL LARGO DEL FONO DEBE SER DE 8 DIGITOS!!")
        crear_fono(user)

usuarios ={
}
crear_cuenta()

def iniciosesion():
    print("!!Bienvenido al menu de usuarios!!\n")
    acceso=int(input("Presione 1 para ver listado de usuarios o presione 0 para generar contraseña e ingresar fono: "))
    if acceso ==1:
        print(list(usuarios))
        volver_menu()
    elif acceso ==0:
        for user in list(usuarios.keys()):
            usuarios[user].append(crear_password())
            usuarios[user].append(crear_fono(user))
    else:
        print("Opcion no valida")
        volver_menu()

def volver_menu():
        print("¿Desea volver al inicio de sesion? ")
        volver=input("Ingrese 0 para volver al menu de inicio de sesion o cualquier tecla para Finalizar: ")
        if volver == "0":
            iniciosesion()
        else:
            print("Esperamos verte pronto...")

iniciosesion()
print("!!CONTRASEÑAS Y FONOS REGISTRADOS!!")
print(usuarios)
print("!!DATOS ALMACENADOS EN BASE DE DATOS!!")
