x=0
def factorial(n):                 
    if n==0 or n==1:               
        return 1                  
    return n*factorial (n-1)
print("¿qué número quiere factorizar?")
x=int(input())
print(factorial(x))               
