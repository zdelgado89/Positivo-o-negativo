# programa para verificar si un numero es positivo o negativo

# imput 

print("-----------------------------------")
X=int(input("digite un numero: "))

# processing

if X > 0:
    rta = "positivo"
    
elif X == 0:
    rta = " su numero es neutro"
    
else:
    rta = " negativo"

# output
print("-----------------------------------")
print("el numero" + str(X) + "es" + rta)
print("-----------------------------------")