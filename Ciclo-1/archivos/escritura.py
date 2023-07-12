import io

fd =open("Ciclo-1/archivos/prueba.txt","w",encoding="utf-8")
lst=["Primera linea\n","Segunda linea\n"]
fd.writelines(lst)
fd.close()