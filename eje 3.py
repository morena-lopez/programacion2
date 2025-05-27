n=0
op=0
bina=0
hexa=0

print("ingrese un numero")
n=int(input())
print("elija si quiere cambiar su numero a binario {1}, hexadecial{2} o si quiere ambos{3}")
op=int(input())

if op==1:
    bina=bin(n)
    print("su numero a lenguaje binario es ",bina)

else:
    if op==2:
        hexa=hex(n)
        print("su numero a lenguaje hexadecimal es ",hexa)

    else:
        if op==3:
            bina=bin(n)
            hexa=hex(n)
            print("su numero en lenguaje binario es ",bina," y su numero a lenguaje hexadecimal es ",hexa)
    

