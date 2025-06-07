n1=0
print("ingrese un numero")
n1=int(input())
if (n1%3==0) and (n1%5==0):
    print("FrizzBuzz")
else:
    if (n1%5==0):
        print("Buzz")
    else:
        if (n1%3==0):
            print("Frizz")
         else:
             print("Error")
