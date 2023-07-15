import json

# midic={1:"Lapiz",2:"Borrador",3:"cuaderno",4:"Lapicero","valor":2500}
midic2={
    "influencers":[{
        "name":"Jaxon",
        "edad":42,
        "Work at":"Tech News"
    },
    {
        "name":"Miller",
        "edad":35,
        "Work at":"It Day"
    }

    ]
}


with open("Ciclo-1/archivos/JSON/diccionarios.json","w")as archivo:
    # json.dump(midic,archivo)
    json.dump(midic2,archivo)
    print("se ha escrito en disco")
    
if not archivo.closed:
    print("Cerrando archivo")
    archivo.close()
    
print("Se ha cerrado el archivo")