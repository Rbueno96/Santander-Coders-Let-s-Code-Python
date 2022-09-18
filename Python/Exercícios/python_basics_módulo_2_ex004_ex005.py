"""Crie um dicionário cujas chaves são os meses do ano e os valores são a
duração (em dias) de cada mês."""

ano_2022 = {'janeiro': 31,
            'fevereiro': 28,
            'março': 31,
            'abril': 30,
            'maio': 31,
            'junho': 30,
            'julho': 31,
            'agosto': 30,
            'setembro': 31,
            'outubro': 30,
            'novembro': 30,
            'dezembro': 31}

print('No ano de 2022:')
"""for k, v in ano_2022.items():
    print(f'O mês de {k} têm {v} dias.')"""

""" Exercício 009 - Imprima as chaves seguidas dos seus valores para dicionário criado no exercício anterior.
Exemplo:
Janeiro - 31
Fevereiro - 28
Março - 31
Etc..."""

for k, v in ano_2022.items():
    print(f'{k} - {v}')
