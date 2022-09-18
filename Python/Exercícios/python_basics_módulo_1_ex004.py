"""Faça um programa que imprima a tabuada do 9 (de 9*1 a 9*10) usando loops."""

numero = str(input('De qual número você deseja ver sua tabuada? '))  #Aqui preciso utilizar o str para ver isnum
if numero.isnumeric():
    numero = int(numero)
else:
    while True:
        print(f'{numero} não é um valor aceito para ver sua tabuada. Digite outro.')
        numero = str(input('De qual número você deseja ver sua tabuada? '))
        if numero.isnumeric():
            numero = int(numero)
            break
        else:
            continue
for c in range(1, 11):
    print(f'{numero} x {c} = {numero * c}')

# Codar com while também, utilizando um contador

"""contador = 0
numero = str(input('De qual número você deseja ver sua tabuada? '))
if numero.isnumeric():
    numero = int(numero)
else:
    while True:
        print(f'{numero} não é um valor aceito para ver sua tabuada. Digite outro.')
        numero = str(input('De qual número você deseja ver sua tabuada? '))
        if numero.isnumeric():
            numero = int(numero)
            break
        else:
            continue
while contador < 10:
    contador += 1
    print(f'{numero} x {contador} = {numero * contador}')"""