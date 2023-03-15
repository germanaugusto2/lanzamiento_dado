# Progrma para calcular el lanxmiento de un dado


print("-------------------------------------")
print("--------LANZAMIENTO DE UN DADO-------")
print("-------------------------------------")

# input

# processing
d1 = random.randint(1.6)
d2 = random.randint(1.6)

d2 = int(input("Adivina el numero que salio en el dado: "))

if (d1==1):
    rta = "UNO"
elif (d1==2):
    rta = "DOS"
elif (d1==3):
    rta = "TRES"
elif (d1==4):
    rta = "CUATRO"
elif (d1==5):
    rta = "CINCO"
elif (d1==6):
    rta = "SEIS"
else: 
    rta = "no es la cara de un dado"

if (d2>b):
    print("usted digito un numero no valido")
else:
    if (d1==d2):
        rta = "Adivinaste el numero"
    else:
        rta = "I AN SORRY... NO ADIVINASTE  "
# output 
print(rta)
print("dado: * +str(d1")
print("listo digme: * str d2")
        
    


    