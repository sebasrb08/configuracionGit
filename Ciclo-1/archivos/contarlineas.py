import io

fd= open("Ciclo-1/archivos/mbox-short.txt","r",encoding="utf-8")
cont=0
for linea in fd:
    cont+=1
fd.close()
print(cont)
