while True:
    try:
        caracter=input("Digite unos caracteres: ")
        listas=""
        cont=0
        flat=True
        if caracter.isalpha():
            break
        else:
            continue
    except:
        print("Error")

while flat==True:

    for i in caracter:
        for l in range(len(caracter)):
            print(l)
            if caracter[l]== i:
                print(caracter[l],i)
                cont+=1    
            if cont == 2:
                listas=i
                caracter=caracter.replace(listas,"",2)

print(caracter)