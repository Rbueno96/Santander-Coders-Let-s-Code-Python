"""Faça um programa que peça um valor monetário e diminua-o em 15%. Seu
programa deve imprimir a mensagem “O novo valor é [valor]”.
"""

valor = float(input('Digite o valor do produto em reais: R$'))
#desconto = float(input('Digite um valor de desconto que será aplicado no valor do produto: (Em %) '))
desconto = 15
valor_final = valor * (1 - (desconto/100))
print(f'O novo valor do produto é {valor_final:.2f}')
