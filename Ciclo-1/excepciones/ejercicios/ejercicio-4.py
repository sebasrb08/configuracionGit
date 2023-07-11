cont=0
while True:
    contraseña=input("Digite contraseña: ")
    if len(contraseña) > 8:
        print("si tiene mas de 8 caracteres")
    else:
        continue
    for letra in contraseña:
        if letra.isdigit() :
            print("si tiene 1 numero")
        else:
            continue
        if letra.islower():
            print("si tiene una en minuscula")
        else:
            continue
        if letra.upper():
            print("si tiene una letra en mayuscula")
        else:
            continue
    if contraseña.strip()!="":
            print("no tiene espacio")
            print("es valido")
            break
    else:
        continue

