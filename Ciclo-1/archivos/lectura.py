import io

# abrirlo
fd =open("Ciclo-1/archivos/texto.txt","r",encoding="utf-8")
fd.seek(52)
# leer = fd.read()
leer2 = fd.readline(7)
leer3 = fd.readlines()

fd.close()
print(leer2.rstrip(),end="*")
print(leer3)

