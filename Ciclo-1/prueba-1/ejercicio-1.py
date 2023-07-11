articulo=int(input("Digite el precio del articulo: "))
cantidad=int(input("Digite cuantas cantidades desea: "))
iva=articulo*cantidad*0.15
precioTotal = articulo*cantidad+iva

if precioTotal > 1000:
    desc= articulo*cantidad * 0.05
    precioTotal=precioTotal-desc

print(f"el precio de la factura es de {precioTotal}")
    