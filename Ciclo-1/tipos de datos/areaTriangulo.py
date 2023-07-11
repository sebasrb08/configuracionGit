# base= float(input('Ingrese base : '))
# altura= float(input('Ingrese la altura: '))
# area=(base*altura)/2
# print("el area del triangulo es :",area)

#ejercicio3

segundos=int(input('ingrese segundos: '))

hora= segundos// 3600
minutos= segundos // 60 - hora*60
segundos2 = segundos % 60
print(int(minutos))
print(int(hora))
print(segundos2)

