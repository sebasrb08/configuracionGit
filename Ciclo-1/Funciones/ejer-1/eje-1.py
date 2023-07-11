def menu():
    while True:
        try:
            print("-"*80)
            print("Menu:")
            print("1.Cantidad de palabras en un string")
            print("2.Calcular el mcd de dos numeros")
            print("3.Calcular el iva de una factura")
            print("4.Salir")
            opcion=int(input("Escoja su opcion: "))
            print("\n")
            print("-"*80)

            if opcion <1 or opcion>4:
                print("Digite un numero valido para la opcion")
                continue
            return opcion
        except ValueError:
            print("ERROR,Numero invalido,Digite un numero")
    
def PalabraString(palabra):
    cont=0
    palabra=palabra.split()
    for i in palabra:
        cont+=1
    palabra=" ".join(palabra)
    print(f"\nla frase {palabra}: tienen {cont} palabras\n")
def mcd():
    while True:
        try:
            a=int(input("Digite un numero: "))
            b=int(input("Digite otro numero: "))
            if a <=0 or b<=0:
                continue
            break
        except ValueError:
            print("\nError,Digite un numero\n")
    if a > b:
        mayor=a
        menor=b
    elif a< b:
        mayor=b
        menor=a

    while menor != 0:
        resultadoMcd = menor
        menor = mayor % menor
    print(f"\nEl MCD es: {resultadoMcd}\n")

def iva(cantidad,iva):
    cantidad=cantidad
    if iva.strip() == "":
        iva=21
    else:
        iva=iva
    iva=int(iva)

    total=(cantidad*(iva/100))+cantidad
    print(f"\nEl total de la factura es: {total}\n")



while True:
    opcion=menu()
    
    if opcion==1:
        while True:
            palabra=input("Ingrese unas palabras: ")
            if palabra.isdigit():
                continue   
            PalabraString(palabra)
            break

    elif opcion==2:
        mcd()
    elif opcion ==3:
        while True:
            try:
                cantidad=int(input("Digite un la cantidad si IVA: "))
                iva2=input("Digite el porcentaje de IVA: ")
                if iva2.isdigit() or iva2.strip()=="":    
                    iva(cantidad,iva2)
                    break
            except ValueError:
                print("Error,Digite un numero")
    elif opcion==4:
        print("Un gusto servirte,hasta luego")
        break
    else:
        print("opcion invalida")
    