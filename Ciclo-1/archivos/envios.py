import io

fd =open("Ciclo-1/archivos/mbox-short.txt","r",encoding="utf-8")
lista=[]
listaNueva=[]
for i in fd:
    if i.count("From:"):
        borrar=i.strip("From:")
        borrar=borrar.rstrip()
        lista.append(borrar)
fd.close()
for l in range(len(lista)-1,0,-1):
    listaNueva.append(lista[l])
    print(f"{lista[l]} \tenviado[ok]")


nuevo =open("Ciclo-1/archivos/nuevo.txt","w",encoding="utf-8")
for h in listaNueva:
    nuevo.writelines(f"{h}\n")
nuevo.close()