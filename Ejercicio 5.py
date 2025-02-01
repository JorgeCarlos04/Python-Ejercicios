#Ejercicoio 5
#  Genera una lista que contenga el cuadrado de los números pares y el cubo de los impares entre 1 y 100 (inclusive). Calcula cuantos números de esa lista debes sumar para que el resultado de la suma sea lo más cercano posible, pero inferior, a un millón.
def lista_de potencias()
list=[]
for i in range (0,100)
    if i%2==0
        list.append(i**2)
    else
        list.append(i**3)

return list

def suma_al_millon(list)
    suma=0
    limite= 1000000
    cont =0
for n in list
    if suma+n<limite
        suma+=n
        cont+=1
return suma,cont


print(f"La suma de los {n} es de {suma_al_millon(list)} y el contador de numeros sumados es de :{cont}")
