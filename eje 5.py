est=0
car=0
numEnt=0
carLoss=0
print("¿cuantos caramelos tienes?")
car=int(input())

print("¿cuantos alumnos hay?")
est=int(input())

numEst=car//est
carLoss=car%est

print("los caramelos que se repartieron fueron ",numEst," por cada estudiante")
print("los caramelos que sobraron fueron : ",carLoss)
