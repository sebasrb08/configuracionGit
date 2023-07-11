def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("Error.Ingrese un numero entero valido")

def leerString(name):
    while True:
        try:
            names=input(name)
            if names.strip() =="":
                print("Digite un nombre valido")
                continue
            return names        
        except Exception as e:
            print("Error al ingresar el nombre",e.message)

def leerPrograma():
    while True:
        try:
            print("1.Tecnico en sistemas")
            print("2.Tecnico en Desarrollo de sistemas")
            print("3.Tecnico en animacion digital")
            programa=int(input("Digite cual es su programa academico: "))
            if programa <0 or programa > 3:
                print("Digite una opcion valida del (1 a 3)")
                continue
            return programa
        except ValueError:
            print("ERROR,Ingrese una opcion valida")        
def beca():
        while True:
            try:
                print("1.Beca por rendimiento academico")
                print("2.Beca Cultural")
                print("3.sin beca")
                beca=int(input("Ingrese el indicador de beca: "))
                if beca <0 or beca > 3:
                    print("Digite una opcion valida del (1 a 3)")
                    continue
                return beca
            except ValueError:
                print("ERROR,Ingrese una opcion valida")  

def valoresMatricula(programa,becas):
    if programa ==1:
        matricula=800000
    elif programa ==2:
        matricula=1000000
    elif programa ==3:
        matricula=1200000
    if becas==1:
        des=50/100
    if becas==2:
        des=40/100
    if becas==3:
        des=0
    valorMatricula=matricula-(matricula*des)
    return valorMatricula

cod=leerInt("Ingrese el codigo del estudiante: ")
nom = leerString("Ingrese el nombre del estudiante: ")
progAcad= leerPrograma()
becas=beca()

valores=valoresMatricula(progAcad,becas)

print("-"*50)
print(f"Nombre:{nom}\nValor neto a pagar de matricula:{valores:,}")
print("-"*50)
