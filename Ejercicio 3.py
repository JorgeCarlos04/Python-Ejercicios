# Obtener un valor de π calculando la suma siguiente para n=200:
#4∑k=1n(−1)k+12k−1
#Ejercicio 3

import math
n=200
suma = 0
def sumatoria(suma,n)
    suma+= 1*n*(-1)*k+12*k-1
    return 4*suma

k=int(imput("Digite el valor de K"))
print (f"EL valor de valor de π es :{sumatoria(suma,n)}")






