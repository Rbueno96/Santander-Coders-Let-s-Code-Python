"""Faça um programa que peça para o usuário digitar uma palavra e imprima
cada letra em uma linha."""

palavra = str(input('Por favor, digite uma palavra: ')).strip().capitalize()
print(f'A palavra {palavra} possui as seguintes letras:')
for l in palavra:
    print(l)