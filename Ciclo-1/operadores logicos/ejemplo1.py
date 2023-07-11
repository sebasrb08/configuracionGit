
# nombre=input("Ingrese nombre: ")
# salario=int(input(f"digite salario de {nombre}: "))
# if salario <= 1200000:
#     subTrans=120000
# else:
#     subTrans=0

# print(f"nombre: {nombre}\nSalario: {salario+subTrans}\nSubsidio de trasnporte: {subTrans}")

# ejercicio2
# nombre= input("Ingrese un nombre: ")
# caliCuantitativa=int(input("Digite la calificacion cuantitativa: "))
# Cualitativa=""
# if caliCuantitativa >= 0 and caliCuantitativa<=59:
#     Cualitativa = "D"
# elif caliCuantitativa >=60 and caliCuantitativa <=79:
#     Cualitativa="C"
# elif caliCuantitativa >=80 and caliCuantitativa <=89:
#     Cualitativa="B"
# elif caliCuantitativa >=90 and caliCuantitativa <=100:
#     Cualitativa="A"
# else:
#     print("Numero no valido")
# if Cualitativa!="":
#     print(f"Nombre: {nombre}\nCalificacion cuantitativa: {caliCuantitativa}\nCalificacion cualitativa: {Cualitativa}")
    
    
#ejercicio3

hora= int(input("Digite hora de el formato de 12 horas: "))
minutos=int(input("digite los minutos en el formato de 12 hora: "))
segundos=int(input("Digite los segundos en el formato de 12 horas: "))
formato=input("Digite si es AM o PM: ")

if formato == "AM" or formato == "PM":
    if formato == "PM":
        if hora!= 12:
            hora= hora + 12
        else:
            hora=hora
    elif formato== "AM":
        if hora == 12 :
            hora=0
    print(f"{hora}:{minutos}:{segundos} {formato}")
else:
    print("error no es ni AM o PM")