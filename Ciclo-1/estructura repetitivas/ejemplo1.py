# for i in range(-1,5,2):
#     print(i,end=", ")

#ejercicio 2

# for i in range(1,101):
#     if i %2==0:
#         print(i,end=", ")

#ejercicio 3

# num =int(input("digite un numero: "))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)

#4

num=int(input("Digite un numero: "))
primo=1
for i in range (1,num):
    if num % i == 0:
        print(i)