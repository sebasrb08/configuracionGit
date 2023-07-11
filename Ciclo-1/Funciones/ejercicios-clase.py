# def leerInt(msg):
#     while True:
#         try:
#             n = int(input(msg))
#             return n
#         except ValueError:
#             print("Error.Ingrese un numero entero valido")

# def media(num1,num2,num3):
#     m=(num1+num2+num3)/3
#     return m

# num1=leerInt("Digite un numero: ")
# num2=leerInt("Digite un numero: ")
# num3=leerInt("Digite un numero: ")

# prom =media(num1,num2,num3)
# print(f"la media de {num1},{num2},{num3} es {prom}")

#ejercicio 2:

def nombre(name):
    while True:
        try:
            names=input(name)
            if names.strip() =="":
                print("Digite un nombre valido")
                continue
            return names        
        except Exception as e:
            print("Error al ingresar el nombre",e.message)

def estrato(estra):
    while True:
        try:
            estra=int(input(estra))
            if estra <1 or estra >5:
                print("Error,Ingrese un estrato valido(1 a 5)")
                continue
            return estra
        except ValueError:
            print("Error,Digite un numero")

def calTarifaBasica(estrato):
    estratos=estrato
    if estratos ==1:
        tarifa=10000
    if estratos ==2:
        tarifa=15000
    if estratos ==3:
        tarifa=30000
    if estratos ==4:
        tarifa=50000
    if estratos ==5:
        tarifa=65000
    return tarifa
name=nombre("Digite un nombre: ")
estra=estrato("Ingrese el estrato del usuario: ")

tarifaBas=calTarifaBasica(estra)
print("-"*50)
print(f"Nombre: {name}\nTarifa Basica:${tarifaBas:,}")
print("-"*50)
