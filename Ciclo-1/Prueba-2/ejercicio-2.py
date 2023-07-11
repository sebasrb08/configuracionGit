dic={}

def menu():
    print("\n")
    print("Nomina ACME")
    print("1.Agregar empleado")
    print("2.Modificar empleado")
    print("3.Buscar empleado")
    print("4.Eliminar empleado")
    print("5.Listar empleados")
    print("6.Listar nomina de un empleado")
    print("7.Listar nomina de todos los empleados")
    print("8.Salir")
    opcion=int(input("digite su opcion: "))
    print("-"*80)
    return opcion

def agEmpleado(dic):
    while True:
        try:
            id=input("Digite su id: ")
            if id.isalpha():
                print("Error,tiene que digitar un numero")
                continue
            nombre=input("Digite su nombre: ")
            horasT=int(input("Digite las horas trabajadas: "))
            if horasT < 1 or horasT > 160:
                print("Error,el rango de horas trabajadas es de (1 a 160)")
                continue
            valorH=int(input("Digite el valor de la hora : "))
            if valorH < 8000 or valorH >150000:
                print("Error,el rango del valor de horas trabajadas es de (8000 a 150000)")
                continue
            dic[id]={}
            dic[id]["nombre"]=nombre
            dic[id]["horasT"]=horasT
            dic[id]["valorH"]=valorH
            
            return dic
        except ValueError:
            print("Error,ingrese un numero valido")
            
def modificarE(dic):
    testigo=True
    while testigo== True:
        try:
            id =(input("Digite el id para el empleado que desea modificar: "))

            print("1.Nombre")
            print("2.Horas Trabajadas")
            print("3.Valor de Hora")
            opcion=int(input("Digite la opcion que desea cambiar: "))
            print("\n")
            if opcion <1 or opcion >3:
                print("Digite una opcion valida")
                continue

            for i in dic.keys():
                indice=-1
                if i == id:
                    indice = i
            if indice != -1:
                if opcion ==1:
                    nombre=input("Digite el nombre que desea cambiar: ")
                    dic[indice]["nombre"]=nombre
                elif opcion ==2:
                    horasT=int(input("Digite las horas trabajadas que desea cambiar: "))
                    dic[indice]["horasT"]=horasT
                elif opcion ==3:
                    valorH=int(input("Digite el Valor de horas trabajadas que desea cambiar: "))
                    dic[indice]["valor"]=valorH
                return dic
            else:
                print("Error,id invalido")
                testigo=False
                
        except:
            print("Error,Digite un numero")

def buscarE(dic):
    id =(input("Digite el id para el empleado que desea buscar: "))
    for i in dic.keys():
        if i == id:
            indice = i
            print("-"*80)
            print(f"Nombre:",dic[indice]["nombre"])
            print(f"Horas Trabajadas:", dic[indice]["horasT"])
            print(f"Valor hora:",dic[indice]["valorH"])
            print("-"*80)

        else:
            print("El usuario no ha sido ingresado")

def eliminarE(dic):
    id =(input("Digite el id para el empleado que desea eliminar: "))
    for i in dic.keys():
        if i == id:
            indice = i
            dic.pop(indice)
            return print("Se ha eliminado correctamente")  
    print("no ha sido eliminado ningun empleado")
    

def listarE(dic):
    cont=0
    for i in dic.keys():
        cont+=1
        seguir=""
        print("-"*80)
        print(f"ID:",i)
        print(f"NOMBRE:",dic[i]["nombre"])
        print(f"HORAS TRABJADAS:",dic[i]["horasT"])
        print(f"VALOR HORA:",dic[i]["valorH"])
        print("-"*80)
        if cont %5==0:
            seguir=input("Desea seguir viendo los 5 siguientes empleados (si / no): ")
        if seguir.upper()=="NO":
            break

def listarNominaU(dic):
    indice=""
    id =(input("Digite el id del empleado que desea ver la nomina: "))
    for i in dic.keys():
        if i == id:
            indice = i
            break
    if indice!="":
        transporte=0
        salario=dic[indice]["horasT"] * dic[indice]["valorH"]
        eps = salario*0.04
        pension= salario * 0.04
        if salario < 1160000:
            transporte=140000
        salarioBr=(salario+transporte-eps)-pension
        salarioNe=salario+transporte
            
        print("-"*80)
        print("\tDATOS:")
        print("ID:",indice)
        print("NOMBRE:",dic[indice]["nombre"])
        print("HORAS TRABJADAS:",dic[indice]["horasT"])
        print("VALOR HORA:",dic[indice]["valorH"])
        print("-"*80)
        print("\t NOMINAS:")
        print(f"Salario Bruto:{salarioBr}")
        print(f"Salario Neto: {salarioNe}")
        print("-"*80)
    else:
        print("Error, no se encontro ningun id")
        


def listarNominaT(dic):
        cont=0
        opcion=""
        for i in dic.keys():
            cont+=1
            transporte=0
            salario=dic[i]["horasT"] * dic[i]["valorH"]
            eps = salario*0.04
            pension= salario * 0.04
            if salario < 1160000:
                transporte=140000
            salarioBr=(salario+transporte-eps)-pension
            salarioNe=salario+transporte
            
            print("-"*80)
            print("\tDatos")
            print("ID:",i)
            print("NOMBRE:",dic[i]["nombre"])
            print("HORAS TRABJADAS:", dic[i]["horasT"])
            print("VALOR HORA:",dic[i]["valorH"])
            print("-"*80)
            print("\t NOMINAS:")
            print(f"Salario Bruto:{salarioBr}")
            print(f"Salario Neto: {salarioNe}")
            print("-"*80)

            if cont % 5==0:
                opcion = input("Desea ver los siguientes empleados (si / no): ")
                if opcion.upper()=="SI":
                        continue
                elif opcion.upper()=="NO":
                    break
                else:
                    print("No indicaste la opcion requerida")
                    break
def salir():
    while True:
        try:
            opcion = input("Desea salir de la aplicacion (si / no)?:")
            if opcion.upper()=="SI":
                return False
            else:
                return True
        except:
            print("Error,Ingrese (si o no)")
testigo=True
while  testigo==True:
    opcion =menu()
    if opcion == 1:
        dic=agEmpleado(dic)
        print(dic)
    elif opcion == 2:
        dic=modificarE(dic)
    elif opcion == 3:
        buscarE(dic)
    elif opcion == 4:
        eliminarE(dic)
    elif opcion == 5:
        listarE(dic)
    elif opcion == 6:
        listarNominaU(dic)
    elif opcion == 7:
        listarNominaT(dic)
    elif opcion == 8:
        testigo=salir()