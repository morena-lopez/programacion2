bille=0
cant=0
miles=0
dos=0
sobr=0
miless=0
opc=""

print("ingrese el dinero a entregar")
cant=int(input())

print("¿quiere solo billetes de $200?¿si o no?")
opc=input()
if opc=="si":
    dos=cant//200
    sobr=cant//200
    print("danos: ",miles," billetes de $1000")
    print("danos: ",dos," billetes de $200")
    print("te sobran: ",sobr)

else:
     if cant>=200:
        dos=cant//200
        sobr=cant%200
        print("danos: ",dos," billetes de $200")
        print("te sobran:$ ",sobr)

     else:
        print("no podes sacar $",cant," en billetes de $200 y $1000")
            
