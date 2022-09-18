"""Faça uma função que recebe duas listas e retorna a soma item a item dessas
listas.
Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve
retornar [1+3, 4+5, 3+1] = [4, 9, 4]."""
def soma_listas():
    primeira_lista = []
    segunda_lista = []
    resultado = []
    print("""Vamos digitar duas listas para somar os valores correspondentes à mesma posição das listas...""")
    for n in range(0, 3):
        numero = str(input(f'Digite o {n+1}º número da primeira lista: '))
        if numero.isnumeric():
            primeira_lista.append(numero)
        else:
            while True:
                print(f'{numero} não é um valor válido para ser atribuído à lista. Digite outro.')
                numero = str(input(f'Digite o {n + 1}º número da primeira lista: '))
                if numero.isnumeric():
                    primeira_lista.append(numero)
                    break
                else:
                    continue
    for n in range(0, 3):
        numero = str(input(f'Digite o {n+1}º número da segunda lista: '))
        if numero.isnumeric():
            segunda_lista.append(numero)
        else:
            while True:
                print(f'{numero} não é um valor válido para ser atribuído à lista. Digite outro.')
                numero = str(input(f'Digite o {n + 1}º número da segunda lista: '))
                if numero.isnumeric():
                    segunda_lista.append(numero)
                    break
                else:
                    continue
        resultado.append(int(primeira_lista[n]) + int(segunda_lista[n]))  # como era str, se somar concatena os valores
    print(resultado)

soma_listas()