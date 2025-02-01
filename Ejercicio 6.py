#Ejercicio 6

def desglose_euros(cantidad):
    billetes = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    desglose = {}
    
    for billete in billetes:
        if cantidad >= billete:
            desglose[billete] = cantidad // billete
            cantidad = cantidad % billete
    
    return desglose

cantidad = int(input("Introduce una cantidad de euros: "))
desglose = desglose_euros(cantidad)
print("Desglose de billetes y monedas:")
for billete, cantidad in desglose.items():
    print(f"{cantidad} x {billete}€")