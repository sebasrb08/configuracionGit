import json

lista=[10,20,30,40,60]

with open("Ciclo-1/archivos/JSON/lista.json","w")as archivo:
    json.dump(lista,archivo)
    print("se ha escrito en disco")
    
if not archivo.closed:
    print("Cerrando archivo")
    archivo.close()
    
print("Se ha cerrado el archivo")
