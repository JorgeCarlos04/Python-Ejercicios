# La variación de temperatura de un cuerpo a temperatura inicial T0 en un ambiente a Ts cambia de la siguiente manera:
#T=Ts+(T0−Ts)  e−kt
#con t en horas y siendo k un parámetro que depende del cuerpo (usemos k=0.45). Una lata de refresco a 5ºC queda en la guantera del coche a 40ºC. ¿Qué temperatura tendrá 1, 5, 12 y 14 horas? Encontrar las horas que hay que esperar para que el cuerpo esté a 0.5ºC menos que la temperatura ambiente. Definir funciones adecuadas para realizar ambos cálculos para cualquier tiempo y cualquier diferencia de temperatura respecto al ambiente respectivamente."""
#Ejercicio 1
import math
import os
def variacion_temperatura_total(T,TS,T0,k,t)
    return T=TS+(T0-TS)*e**(-k*t)

def diferencia(TS,t,T0,k)
    return t+TS/k

k=0,45
TS=imput("Ingrese la temperatura ambiente")
T0=imput("Ingrese la temeperatura inicial")
float(TS)*2
float(T0)*2


tiempo=tiempo[1,5,12,14]
for time in time
    print(f"La temperatura al cabo de{time} es de {variacion_temperatura_total(T,TS,T0,k,t)}")

print(f"El tiempo d espera estimado para que se encuentre a menos 0,5 gardos menoses de {diferencia(TS,t,T0,k)}")






