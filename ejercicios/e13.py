M = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
]

n = 4
suma_principal = 0
suma_secundaria = 0

print("Matriz 4x4:")
for i in range(n):
    for j in range(n):
        print(M[i][j], end="\t")
        if i == j:  
            suma_principal += M[i][j]
        if i + j == n - 1:  
            suma_secundaria += M[i][j]    
    print()

print("Suma diagonal principal:", suma_principal)
print("Suma diagonal secundaria:", suma_secundaria)
