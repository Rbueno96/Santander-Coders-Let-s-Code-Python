"""Faça um programa que olhe todos os itens de uma lista e diga quantos deles
são pares."""

import random
numeros = []
pares = []
quantidade_pares = 0
for c in range(0, 8):
    numeros.append(random.randint(0, 11))
for v in numeros:
    if v % 2 == 0:
        pares.append(v)
        quantidade_pares += 1
print(numeros)
print(f'Essa lista tem {quantidade_pares} números pares e são eles {pares}.')
