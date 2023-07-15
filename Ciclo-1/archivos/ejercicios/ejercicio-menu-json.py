import io
import json

def error():
  fd = open("emplacme.json","a")
  fd.close


def almacenamiento():
    try:
      fd = open("emplacme.json","r+")
      dic={}
      leer=json.load(fd)
      for s in leer.keys():
            dic[s]={}
            dic[s]["nombre"]=leer[s]["nombre"]
            dic[s]["horasT"]=leer[s]["horasT"]
            dic[s]["valorH"]=leer[s]["valorH"]
        
      fd.close()
      return dic
    except:
      error()
      dic={}
      return dic


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
            flat=False
            for i in dic.keys():
                if id == i:
                    print("error ingrese otro id,el id ya esta:")
                    flat=True
            if flat == True:
                continue
            
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
            
            fd = open("emplacme.json","w")
            agregar=json.dump(dic,fd)
            
            fd.close()
            return dic
        except ValueError:
            print("Error,ingrese un numero valido")
            
def modificarE(dic):
            id =(input("Digite el id para el empleado que desea modificar: "))

            print("1.Nombre")
            print("2.Horas Trabajadas")
            print("3.Valor de Hora")
            opcion=int(input("Digite la opcion que desea cambiar: "))
            print("\n")
            if opcion <1 or opcion >3:
                print("Digite una opcion valida")
                
            for i in dic.keys():
                if i == id:
                    indice = i
            if opcion ==1:
                nombre=input("Digite el nombre que desea cambiar: ")
                dic[indice]["nombre"]=nombre
            elif opcion ==2:
                horasT=int(input("Digite las horas trabajadas que desea cambiar: "))
                dic[indice]["horasT"]=horasT
            elif opcion ==3:
                valorH=int(input("Digite el Valor de horas trabajadas que desea cambiar: "))
                dic[indice]["valorH"]=valorH
                    
            borrarModi(dic)
            return dic


def buscarE(dic):
    flat=True
    id =(input("Digite el id para el empleado que desea buscar: "))
    for i in dic.keys():
        if i == id:
            indice = i
            print("-"*80)
            print(f"Nombre:",dic[indice]["nombre"])
            print(f"Horas Trabajadas:", dic[indice]["horasT"])
            print(f"Valor hora:",dic[indice]["valorH"])
            print("-"*80)
            flat=False
    if flat == True:
        print("Error,el usuario no ha sido ingresado")
        
        
def eliminarE(dic):
    id =(input("Digite el id para el empleado que desea eliminar: "))
    for i in dic.keys():
        if i == id:
            indice = i
            dic.pop(indice)
            borrarModi(dic)
            return print("Se ha eliminado correctamente")  
    print("no ha sido eliminado ningun empleado")
    

def listarE(dic):
    cont=0
    for i in dic.keys():
        cont+=1
        seguir=""
        if cont %6==0:
            seguir=input("Desea seguir viendo los 5 siguientes empleados (si / no): ")
        if seguir.upper()=="NO":
            break
        print("-"*80)
        print(f"ID:",i)
        print(f"NOMBRE:",dic[i]["nombre"])
        print(f"HORAS TRABJADAS:",dic[i]["horasT"])
        print(f"VALOR HORA:",dic[i]["valorH"])
        print("-"*80)
        

def listarNominaU(dic):
    indice=""
    id =(input("Digite el id del empleado que desea ver la nomina: "))
    for i in dic.keys():
        if i == id:
            indice = i
            break
    if indice!="":
        transporte=0
        salario=int(dic[indice]["horasT"]) * int(dic[indice]["valorH"])
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
            if cont % 6==0:
                opcion = input("Desea ver los siguientes empleados (si / no): ")
                if opcion.upper()=="SI":
                        pass
                elif opcion.upper()=="NO":
                    break
                else:
                    print("No indicaste la opcion requerida")
                    break
            transporte=0
            salario=int(dic[i]["horasT"]) * int(dic[i]["valorH"])
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
            
def borrarModi(dic):
    fd = open("emplacme.json","w+")
    nuevo=json.dump(dic,fd)    
    fd.close()
  
dic=almacenamiento()
testigo=True
while  testigo==True:
    opcion =menu()
    if opcion == 1:
        dic=agEmpleado(dic)
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