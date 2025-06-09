import math

vol=0
rad=0
alt=0
op=""
print("elija una opcion")
print("A) sacar el area de un circulo")
print("B) sacar volumen de un cilindrico")
op=input()

if op=="A":
    print("digame el radio de un circulo")
    rad=int(input())

    area=(rad**2)*math.pi
    print("la area del circulo es: ",area)

else:
    print("cuanto mide el radio de su cilindro")
    rad=int(input())
    print("cuanto mide el alto de su cilindro")
    alt=int(input())

    area=(radio**2)*math.pi
    vul=area*alt
    print("el vulumen del cilindrio es: ",vul)
