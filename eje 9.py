ci=0
num=0
si=0

for x in range (1,4,1):
    print("ingrese el ",x," numero")
    num=int(input())
    if ((num%2)==1):
        ci=ci+1
        si=si+num

print("la cantidad de numeros impares es ",ci)
print("la suma de los numeros impares es ",si)
