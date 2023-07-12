import io

fd= open("Ciclo-1/archivos/mbox-short.txt","r",encoding="utf-8")
cont=0
for linea in fd:
    line=linea.rstrip()
    if not "@uct.ac.za"in line:
        continue
    print(line)
fd.close()

