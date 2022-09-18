"""Ex004 - Você conhece Star Wars? Se trata, obviamente, da famosa saga espacial criada por George Lucas em 1977 e que
deu origem a símbolos do cinema e da cultura pop com o imponente vilão Darth Vader ou o simpático robô R2-D2.
A ideia desse exercício é justamente extrair informações do personagem Darth Vader através de uma API de Star Wars
chamada SWAPI. Utilize a URL "https://swapi.dev/api/people/4/" para fazer a requisição dos dados de Darth Vader e
extraia as informações "name" (nome), "height" (altura), "mass" (massa) e "birth_year" (ano de nascimento) e imprima
cada dado em uma linha.
Dica: caso não se lembre de como fazer isso, assista novamente a aula sobre
API porque o exemplo da aula pode te ajudar"""

import requests
url = 'https://swapi.dev/api/people/4/'
requisicao = requests.get(url)
#print(requisição)  # Apenas para verificar se a URL está respondendo
raw_data = requisicao.json()  #JavaScript Object Notation é uma um formato leve de troca de informações entre sistemas...
final_data = []
for k, v in raw_data.items():
    if k == 'name':
        print(f'{k} : {v}')
        final_data.append(f'{k} : {v}')
    elif k == 'height':
        print(f'{k} : {v}')
        final_data.append(f'{k} : {v}')
    elif k == 'mass':
        print(f'{k} : {v}')
        final_data.append(f'{k} : {v}')
    elif k == 'birth_year':
        print(f'{k} : {v}')
        final_data.append(f'{k} : {v}')
print(final_data)

"""for obs in raw_data:
    final_data.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])
    
    PRECISO SABER POR QUE DESSA FORMA DEU CERTO NO PROJETO DA AULA 18 E AQUI NÃO"""
# Ainda vou tentar retirar do raw_data e adicionar a uma outra lista ou a um outro dicionário