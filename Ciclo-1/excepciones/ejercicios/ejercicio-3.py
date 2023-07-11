
while True:
    frase=input("Digite una frase: ")
    i=0
    cont=0
    vocales="AEIOU"
    flat= True
    if frase.strip()=="":
        continue
    else:
        break

while flat== True :
    vocales=" ".join(vocales)
    vocales = vocales.split()
    while i < len(frase):
        letra= frase[i].upper()
        if frase[i].upper() in vocales:
            cont+=1
        if frase[i].upper() =="Q":
            flat=False
            break
        i+=1
    

        


print(f"Hay {cont} vocales")