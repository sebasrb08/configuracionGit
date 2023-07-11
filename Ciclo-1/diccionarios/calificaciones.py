dic={}

def codigo():
    while True:
        try:
            codi=float(input("Digite el Codigo: "))
            return codi
        except ValueError:
            print("Error,Ingrese un nu")

def nom():
    while True:
        try:
            nombre=input("Digite el Nombre: ")
            if nombre.isdigit():
                print("Error,digite un numero valido")
                continue
            return nombre
        except ValueError:
            print("Error,Ingrese un nu")
            
            
def aprobacion(nota):
    if nota >= 3.0:
        print("-"*80)
        print("Aprobado")
        print("-"*80)
        
    else:
        print("-"*80)
        print("No aprobo")
        print("-"*80)

    
while True:
    codi=codigo()
    
    if codi== 999:
        break
        
    nombre=nom()
    nota1=float(input("digite nota 1: "))
    nota2=float(input("digite nota 2: "))
    nota3=float(input("digite nota 3: "))
    dic[codi]={}
    dic[codi]["nombre"]=nombre
    dic[codi]["nota1"]=nota1
    dic[codi]["nota2"]=nota2
    dic[codi]["nota3"]=nota3
    notaF=(dic[codi]["nota1"]*0.30)+(dic[codi]["nota2"]*0.30)+(dic[codi]["nota3"]*0.40)
    dic[codi]["notaFinal"]=notaF
    aprobacion(notaF)
    
print("Notas de todos")
for k in dic.keys():
    print("Nombre: ",dic[k]["nombre"])
    print("Nota 1: ",dic[k]["nota1"])
    print("Nota 2: ",dic[k]["nota2"])
    print("Nota 3: ",dic[k]["nota3"])
    print("Nota final: ",dic[k]["notaFinal"])
    print("-"*30)    