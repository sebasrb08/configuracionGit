num=int(input("Digite un numero"))
cont=0
while num > 0:
    for i in range(1,num):
        if num % i ==0:
            cont+=1
        if cont == 2:
            primos=i
            print(primos)            
    num=int(input("Digite un numero"))

        
        