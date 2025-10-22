import random

alum=["nicol","mara","mateo","luana","benja","sara","gennaro","tomas","lucy","trini"]
print("LISTA DE ESTUDIANTES")
print(alum)


for x in range (len(alum)):
    nom=random.choice(alum)
    print("el elejido a pasar es: ", nom, )
    alum.remove(nom)


    
    
