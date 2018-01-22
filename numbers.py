# suma los i divisibles por 3 y 5
import math

total = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print("total = ", total)

print("-" * 90)

lista = []  # imprime lista numeros divisibles por x
for i in range(1, 100):
    if i % 3 == 0:
        lista.append(i)
print(lista)


print("-" * 90)

# list comprehension de numeros impares
tuplaLC_impares = [i for i in range(1, 100, 2)]
# list comprehension de numeros pares
tuplaLC_pares = [i for i in range(0, 100, 2)]
tuplaLC_pares.remove(0)

tuplaLCif = tuple(g**2 for g in range(0, 20, 1) if g **
                  2 < 100)  # cuadrados menores de 100
listaLCif = [pow(g, 3) for g in range(1, 10, 1) if g <=
             6]  # cubos de numeros menores a 7
# raiz2 de numeros menores a 7
listaLCif2 = [math.sqrt(g) for g in range(1, 10, 1) if g <= 6]
listaLCif3 = [pow(h, 1. / 3.) for h in range(1, 27, 1)]  # raiz3 debe ajustarse
a = 9
b = a**(1. / 3.)
print("b= ", b)  # wtf  en raiz cubica tiene que ajustarse la exactitud

print(tuplaLC_impares)
print(tuplaLC_pares)
print("-" * 90)
print(tuplaLCif)
print("-" * 90)
print(listaLCif)
print("-" * 90)
print(listaLCif2)
print("-" * 90)
print(listaLCif3)
