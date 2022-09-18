"""Vamos fazer um programa para verificar quem é o assassino de um crime.
Para descobrir o assassino, a polícia faz um pequeno questionário com 5
perguntas onde a resposta só pode ser sim ou não:
a. Mora perto da vítima?
b. Já trabalhou com a vítima?
c. Telefonou para a vítima?
d. Esteve no local do crime?
e. Devia para a vítima?

Cada resposta sim dá um ponto para o suspeito. A polícia considera que os
suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices e
2 pontos são apenas suspeitos, necessitando outras investigações. Valores
iguais ou abaixo de 1 são liberados."""
pontuação = 0
suspeitos = {}
lista_suspeitos = []
for cada in range(0, 3):
    pontuação = 0
    suspeitos['nome'] = str(input('Qual é o nome do suspeito? ')).strip().capitalize()
    while True:
        resp_A = input(f'O {suspeitos["nome"]} mora perto da vítima? ').strip().lower()
        if resp_A == 'sim':
            pontuação += 1
            break
        elif resp_A == 'não' or resp_A == 'nao':
            break
        else:
            print('Resposta inválida. Diga sim ou não.')
            continue
    while True:
        resp_B = input(f'O {suspeitos["nome"]} já trabalhou com a vítima? ').strip().lower()
        if resp_B == 'sim':
            pontuação += 1
            break
        elif resp_B == 'não' or resp_B == 'nao':
            break
        else:
            print('Resposta inválida. Diga sim ou não.')
            continue
    while True:
        resp_C = input(f'O {suspeitos["nome"]} telefonou para a vítima? ').strip().lower()
        if resp_C == 'sim':
            pontuação += 1
            break
        elif resp_C == 'não' or resp_C == 'nao':
            break
        else:
            print('Resposta inválida. Diga sim ou não.')
            continue
    while True:
        resp_D = input(f'O {suspeitos["nome"]} esteve no local do crime? ').strip().lower()
        if resp_D == 'sim':
            pontuação += 1
            break
        elif resp_D == 'não' or resp_D == 'nao':
            break
        else:
            print('Resposta inválida. Diga sim ou não.')
            continue
    while True:
        resp_E = input(f'O {suspeitos["nome"]} devia para a vítima? ').strip().lower()
        if resp_E == 'sim':
            pontuação += 1
            break
        elif resp_E == 'não' or resp_E == 'nao':
            break
        else:
            print('Resposta inválida. Diga sim ou não.')
            continue
    suspeitos['pontuação'] = pontuação
    if pontuação == 5:
        suspeitos['consideração'] = 'assassino'
    elif 5 > pontuação >= 3:
        suspeitos['consideração'] = 'cúmplice'
    elif pontuação == 2:
        suspeitos['consideração'] = 'suspeito'
    elif pontuação <= 1:
        suspeitos['consideração'] = 'liberado'
    lista_suspeitos.append(suspeitos.copy())
for suspeito in lista_suspeitos:
    for k, v in suspeito.items():
        print(f'O {k} é {v}')