import io
import json


def cargarInfo():
    try:
        dic={}
        with open("estudiantes.json","r+")as archivo:
            
            dic = json.load(archivo)
            return dic
    except:
        dic={}
        return dic


def menu():
    while True:
        try:
            print("""
\tMenu:
1.Estudiantes
2.Notas
3.Reportes
4.salir 
                """)
            
            opcion=int(input("Ingrese su opcion: "))
            if opcion <1 or opcion >4:
                print("!Error¡,digite una opcion valida")
                continue
            return opcion
        except ValueError:
            print("Error,digite un numero")

def estudiantes(dic):
    while True:
        try: 
            print("""
\tEstudiantes
1.Agregar
2.Modificar
3.Eliminar
4.Buscar
5.Salir 
                """)
            opcion=int(input("Ingrese su opcion: "))
            if opcion<1 and opcion>5:
                print("Error,digite una opcion valida")
                continue
            if opcion==1:
                dic=agEstudiantes(dic)
            elif opcion == 2:
                dic=modiEstudiantes(dic)
            elif opcion== 3:
                busqEstudiantes(dic)
            elif opcion==4:
               dic = elimEstudaintes(dic)
            
            elif opcion==5:
                break
            
            return dic
            
        except:
            print("Error,digite un numero")
            continue
        
def agEstudiantes(dic):
    while True:
        try:
            id=int(input("Digite el id del estudiante : "))
            
        except ValueError:
            print("Error,Digite un id valido")
            continue
            
        try:
            nombre=input("Digite el nombre del estudiante: ")
            if not nombre.isdigit:
                print("Error,los numeros no son validos")
                continue
        except:
            print("Error,Digite un nombre valido")
            continue
        
        try:
            sexo=input("Ingrese el sexo del estudiante(h/m): ")
            # if sexo.upper() != "H" or sexo.upper() != "M":
            #     print("ERROR,Ingrese un sexo valido")
            #     continue
            
        except ValueError:
            print("Error,Digite un sexo valido")
            continue
        try:
            grado=input("Ingrese el grado del estudiante: ")
            for i in dic.keys():
                if grado == i:
                    pass
                else:
                    dic[grado]={}
        except Exception as e:
            print("Error,Digite un grado valido")
            continue
        dic[grado][id]={}
        dic[grado][id]["nombre"]=nombre
        dic[grado][id]["sexo"]=sexo
        
        with open("estudiantes.json","w")as archivo:
            enviar=json.dump(dic,archivo)
        return dic   

def modiEstudiantes(dic):
    while True:
        try:
            id=int(input("Digite el id del estudiante que desea cambiar : "))
            for i in dic.keys():
                for l in dic[i].keys():
                    if id != dic[i][l]:
                        print("Error,Digite un id valido")
                        continue
        except ValueError:
            print("Error,Digite un id valido")
            continue
        try:
            print("""

1.Nombre
2.Sexo
4.Grado
5.Salir 
                """)
            opcion=int(input("Digite la opcion que desea modificar: "))
        except:
            print("ERROR")

def notas(dic):
    cont=0
    while True:
        try:
            curso=input("Digite el curso : ")
            for i in dic.keys():
                if curso != dic[i]:
                    print("Error")
        except ValueError:
            print("Error,Digite un curso valido")
            continue
        
        for l in dic[curso].keys():
                cont+=1
                dic[i][l]["nombre"]=sorted(dic[curso][l]["nombre"])
                print(f"{cont}.",dic[curso][l]["nombre"])

def reportes():
    pass

def salir():
    pass

dic=cargarInfo()
while True:
    opcion=menu()
    
    if opcion==1:
        dic=estudiantes(dic)
    elif opcion == 2:
        dic=notas(dic)
    elif opcion== 3:
        reportes()
    elif opcion==4:
        salir()