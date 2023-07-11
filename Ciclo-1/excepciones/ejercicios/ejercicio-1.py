import random
while True:
    try:
        usuario=int(input("Digite cuantos usuarios van a jugar: "))
        i=0
        flat=False
        nombreNuevo=''
        break
    except ValueError:
        print("ERROR,numero invalido")

while i !=usuario:
    cont=1
    while True:
        try:
            nombre=input("Digite su nombre: ")
            num=int(input("digite un numero: "))
            aleatorio=random.randrange(1,101)
            oportunidades=random.randrange(3,6)
            menor=float('inf')
            if num <= 0 or num >100:
                print("Digite un numero entre 0 a 100")
                continue
            break
        except ValueError:
            print("!ERROR¡.Digite un numero")

   
    while aleatorio!=num and oportunidades != cont:
            
        if aleatorio>num:
            print("esta bajo")
        elif aleatorio<num:
            print("esta alto")
        num=int(input("digite un numero: "))
        cont+=1
  
    if aleatorio== num:
        print("adivinaste el numero")
        if menor > cont:
            menor=cont
            nombreNuevo=nombre
            flat = True
    else:
        print("se te acabaron las opurtunidades")
        print(f" el numero era {aleatorio}")
    i+=1

if flat:
    print(f"el ganador es {nombreNuevo} con {menor} intentos")
else:
    print("ninguno gano")