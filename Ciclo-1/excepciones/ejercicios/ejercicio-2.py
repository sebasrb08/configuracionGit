
while True:
    oracion=input("Digite una oracion: ")
    clave=input("Digite una palabra clave: ")
    if clave.strip()== "" or oracion.strip() == "":
        continue
    elif clave.upper== "SALIR":
        break
    else:
        encontrar=oracion.find(clave)
        if encontrar !=-1:
            print("mensaje exitoso")
            break
        else:
            print("mensaje no exitoso")
            continue
        