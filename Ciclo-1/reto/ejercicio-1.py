import io
import json


def menu():
    while True:
        try:
            print("""
\tMenu:
1.Productos
2.Factura
3.informe
4.salir 
                """)
            
            opcion=int(input("Ingrese su opcion: "))
            if opcion <1 or opcion >4:
                print("!Error¡,digite una opcion valida")
                continue
            return opcion
        except ValueError:
            print("Error,digite un numero")

def producJson():
    try:
        dic={}
        with open("productos.json","r+")as archivo:
            leer=json.load(archivo,)
            dic=leer
            return dic
    except:
        dic={}
        return dic

     
def productos(dic):
    while True:
        try:
            id=int(input("Digite el codigo del producto: "))
        except ValueError:
            print("Error,Digite un id valido")
            continue
            
        try:
            nombre=input("Digite el nombre del producto: ")
            if not nombre.isdigit:
                print("Error los numeros no son validos")
                continue
        except:
            print("Error,Digite un nombre valido")
            continue
        
        try:
            valorU=int(input("Digite el valor del producto: "))
        except ValueError:
            print("Error,Digite un valor valido")
            continue
        
        try:
            print("""
\tTipo de iva:
1.Excendente
2.Bienes
3:General
                  """)
            
            categoriaIva=int(input("Digite su opcion: "))
            categorias={1:0,2:0.05,3:0.19}
        except ValueError:
            print("Error,Digite un tipo de iva valido")
            continue
        dic[id]={}
        dic[id]["nombre"]=nombre
        dic[id]["valor"]=valorU
        dic[id]["categoria"]={}
        dic[id]["categoria"]=categorias[categoriaIva]
    
        with open("productos.json","w+")as archivo:
            enviar= json.dump(dic,archivo)
        
        return dic        
            
def facturaJson():
    try:
        dicFactura={}
        with open("facturas.json","r+")as archivo:
            leer=json.load(archivo)
            dicFactura=leer
            return dicFactura
    except:
        dicFactura={}
        return dicFactura           
            
def ventas(dic,dicFactura):
    cantidad={}
    cont=0
    valorTotal=0
    valorIvaTotal=0
    while True:
        try:
            if cont ==0:
                id=int(input("Digite el DNI del Cliente: "))
                dicFactura[id]={}
            else:
                pass
            
        except ValueError:
            print("Error,Ingrese un DNI valido")
            continue
        
        try:
            flat=False
            idProducto=input("Digite el codigo del Producto: ")
    
            for l in dic.keys():
                if idProducto == str(l):
                    flat=True
            if flat== False:
                print("el producto no existe")
                continue
            
        except ValueError:
            print("Error el producto no existe")
            break
        
        
        try:
            cantidad[idProducto]["cantidad"]+=1
        except:
            cantidad[idProducto]={}
            cantidad[idProducto]["cantidad"]=0
            cantidad[idProducto]["cantidad"]+=1
        
        
        valorP=cantidad[idProducto]["cantidad"]*dic[idProducto]["valor"]
        
        valorIva=dic[idProducto]["categoria"]*valorP
        valoresIva=valorIva+valorP
        
        valorTotal+=valoresIva
        
        dicFactura[id][idProducto]={}
        dicFactura[id][idProducto]["valorP"]=valorP
        dicFactura[id][idProducto]["valoresIva"]=valoresIva
        dicFactura[id][idProducto]["valorIva"]=valorIva
                
        opcion=input("Desea seguir ingresando Productos (si no) ? : ")
        cont=1
        if opcion== "si":
            continue
        else:
            dicFactura[id]["valorF"]=valorTotal
            for t in dicFactura[id].keys():
                if t.isdigit():
                    valorIvaTotal+=dicFactura[id][t]["valorIva"]
            dicFactura[id]["valorIvaTotal"]={}
            dicFactura[id]["valorIvaTotal"]=valorIvaTotal
            
            with open("facturas.json","w+")as archivo:
                enviar=json.dump(dicFactura,archivo) 
            imprimirFact(dicFactura,dic,id)
            break

def imprimirFact(dicFactura,dic,ids):
  print("\tFACTURA:")
  for d in dicFactura[ids].keys():
      if d.isdigit():
        print("-"*50)
        print("Codigo:",d,end=",")
        print("Nombre:",dic[d]["nombre"],end=",")
        print("Valor por unidad:",dic[d]["valor"],end=",")
        print("Iva:",int(dic[d]["categoria"]*100),"%")
        print("Valor Producto:",dicFactura[ids][d]["valorP"])
        print("Valor con Iva:",dicFactura[ids][d]["valoresIva"])
        print("-"*50)

  print("Valor Total: :",dicFactura[ids]["valorF"])
  print("Valor Total IVA:",dicFactura[ids]["valorIvaTotal"])
  print("-"*50)


def informe():
    pass

dic=producJson()
dicFactura=facturaJson()
while True:
    opcion=menu()
    
    if opcion==1:
        dic=productos(dic)
    elif opcion == 2:
        ventas(dic,dicFactura)
    elif opcion== 3:
        informe()
    elif opcion==4:
        salir()