a=int(input("Digite el lado de un triangulo: "))
b=int(input("Digite el lado de un triangulo: "))
c=int(input("Digite el lado de un triangulo: "))

p= (a+b+c)/2
area= (p*(p-a)*(p-b)*(p-c))**0.5

print(f"el area es {area:.2f}")

if p > a and p > b and p > c:
    triangulo="si es un triangulo"
else:
    triangulo="no es un triangulo"
    
print(triangulo)

