num=int(input("Digite un numero: "))
i=0
acumulador=0
while i != num:
    i+=1
    if num % i==0 and num != i:
        acumulador+=i 
if acumulador == num:
    print("es un numero perfecto")
else:
    print("no es un numero perfecto")       