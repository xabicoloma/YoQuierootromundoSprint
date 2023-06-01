def crear_fono():
    print(f"A continuacion debe ingresar un fono para de 8 digitos numericos")
    fono=int(input(f"ingresar fono asignado para : "))
    verificador_fono=str(fono)
    if len(verificador_fono) == 8:
        print("Fono registrado")
    else:
        print("!!Fono es demasiado Corto!!")
        crear_fono()
crear_fono()