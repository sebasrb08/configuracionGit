def menu():
    while True:
        try:
            opcion=int(input("\n1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir\n5.potencia\n6.Facotrial\n7Salir\nDigite su opcion: "))
            if opcion < 1 or opcion > 7:
                msgError("Opcion no valida")
                continue
            return opcion
        except ValueError:
            print("Error,Digite un numero")
def sumar():
    while True:
        try:
            num1=int(input("Digite un numero: ")) 
            num2=int(input("Digite un numero: ")) 
            sumas=num1+num2
            return sumas
        except ValueError:
            msgError("Error,Digite un numero")

    

def restar():
    while True:
        try:
            num1=int(input("Digite un numero: ")) 
            num2=int(input("Digite un numero: ")) 
            resta=num1-num2
            return resta
        except ValueError:
            msgError("Error,Digite un numero")
 
def multiplicar():
    while True:
        try:
            num1=int(input("Digite un numero: ")) 
            num2=int(input("Digite un numero: ")) 
            multiplicar=num1*num2
            return multiplicar
        except ValueError:
            msgError("Error,Digite un numero")
 
def dividir():
    while True:
        try:
            num1=int(input("Digite un numero: ")) 
            num2=int(input("Digite un numero: "))
            dividir=num1/num2
            return dividir
        except ValueError:
            msgError("Error,Digite un numero")
        except ZeroDivisionError:
            msgError("Error,el 0 no puede")
 
def potencia():
    while True:
        try:
            num1=int(input("Digite un numero: ")) 
            num2=int(input("Digite un numero: ")) 
            potencia=num1**num2
            return potencia
        except ValueError:
            msgError("Error,Digite un numero")
 
def factorial():
    while True:
        try:
            multi=1
            num1=int(input("Digite un numero: ")) 
            for i in range(1,num1+1):
                multi*=i
            return multi
        except ValueError:
            msgError("Error,Digite un numero")

def msgError(msg):
    print(msg)
while True:
    opcion=menu()
    
    if opcion ==1:
        print(f"\n{sumar()}")
    elif opcion ==2:
        print(f"\n{restar()}")
    elif opcion ==3:
        print(f"\n{multiplicar()}")
    elif opcion ==4:
        print(f"\n{dividir()}")
    elif opcion == 5:
        print(f"\n{potencia()}")
    elif opcion ==6:
        print(f"\n{factorial()}")
    elif opcion ==7:
        print("Gracias por usar la minicalculadora")
        break