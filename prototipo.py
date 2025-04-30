
#se podria implementar una cola mas sofisticada
cola = ["Ø"]

cadena = str(input("Ingresa una cadena: "))

for caracter in cadena:
    cola.append(caracter)

cola.append("Ø")

print(cola)

def estado_0(cola):
    if(cola[0] == "Ø"):
        estado_1(cola, 1)


def estado_1(cola, i):
    if(cola[i] == "a"):
        cola[i] = "Ø"   
        estado_2(cola, "a", i)

    elif(cola[i] == "b"):
        cola[i] = "Ø"
        estado_2(cola, "b", i)
        
    elif(cola[i] == "c"):
        cola[i] = "Ø"
        print("Cadena correcta")
    else:
        print("Cadena invalida")

def estado_2(cola, caracter, i):
    j = i
    while(cola[j+1] != "Ø"):
        j += 1
    if(cola[j] == caracter):
        cola[j] = "Ø"
        estado_3(cola, j)
    else:
        print("Cadena invalida")

def estado_3(cola, j):
    i = j
    while(cola[i-1] != "Ø"):
        i -= 1

    estado_1(cola, i)
    
estado_0(cola)
print(cola)
    



