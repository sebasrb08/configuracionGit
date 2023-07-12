import io

# abrirlo
fd =open("Ciclo-1/archivos/texto.txt","a+",encoding="utf-8")
fd.seek(52)
# leer = fd.read()
# leer2 = fd.readline(7)
# leer3 = fd.readlines()
leer4=fd.write("hola que tal vas\nque mas")
leer5 = fd.read()
fd.close()

print(leer4)

