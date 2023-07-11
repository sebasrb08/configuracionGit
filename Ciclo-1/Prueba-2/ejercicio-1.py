def caracter():
    while True:
        try:
            caracteres=input("Digite una serie de caracteres: ")
            if 3 < len(caracteres) and len(caracteres) < 10**4: 
                return caracteres
            else:
                print("Error,tiene que tener al menos 3 caracteres")
                continue
          
        except:
            print("Error,digite un caracter correct")
letra=[]
contador=[]
caracteres=caracter()
cont=0
caracteres=" ".join(caracteres)
caracteres=caracteres.split()
for i in range(len(caracteres)):

    cont=0
    for l in range(len(caracteres)):
        if caracteres[l]== caracteres[i]:
            cont+=1
    if cont >= 2  :
        letra.append(caracteres[i])
        contador.append(cont)


letra.sort(key=len)
for k in range(len(letra)):
    print(letra[k],contador[k])
    
            
    