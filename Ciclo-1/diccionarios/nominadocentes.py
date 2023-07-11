diccionario_categoria={1:25000,
                       2:30000,
                       3:40000,
                       4:45000,
                       5:60000}
totHonor = 0
docentes ={}
while True:
    cedula=int(input("Ingrese la cedula del docente: "))
    nombre=input("Ingrese el nombre del docente: ")
    categoria= int(input("Categoria del Docente:"))
    horas=int(input("Horas laboradas en el mes por el docente: "))
    docentes[cedula]={}
    docentes[cedula]["nombre"]=nombre
    docentes[cedula]["categoria"]=categoria
    docentes[cedula]["horas"]=horas
    print(docentes)
    opc=input("Dese agregar otro docente(S/N)?: ")
    if opc.lower()=="n":
        break
print("\n\n Informe")
print("-"*30)
for k in docentes.keys():
    h =docentes[k]["horas"] * diccionario_categoria[docentes[k]["categoria"]]
    totHonor+=h
    print(docentes[k]["nombre"], f"--${h:,}")
print(f"Total honorarios de los docentes: {totHonor:,}")