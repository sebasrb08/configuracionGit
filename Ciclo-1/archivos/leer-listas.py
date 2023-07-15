import json

with open("Ciclo-1/archivos/JSON/diccionarios.json","r")as archivo:
    # json.dump(midic,archivo)
    lista=json.load(archivo)
    print("se ha escrito en disco")
    
if not archivo.closed:
    print("Cerrando archivo")
    archivo.close()

for elem in lista:
    print(lista[elem][1]["name"])
    
print("Se ha cerrado el archivo")