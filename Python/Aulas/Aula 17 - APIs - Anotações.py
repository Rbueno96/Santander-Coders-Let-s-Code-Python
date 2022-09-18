# O primeiro passo para utilizar uma API é ler sua documentação
import requests
url = 'https://api.exchangerate-api.com/v6/latest'
requisição = requests.get(url)
# print(requisição.status_code)  # Código de status 200 significa que está ok, codigo do status

dados = requisição.json()  #json é uma um formato leve de troca de informações entre sistemas
# criada em JavaScript Object Notation
print(dados)
# Nesse programa vamos criar um conversos monetário:
valor_reais = float(input('Informe o valor em reais: \nR$'))
cotação = dados['rates']['BRL']
print(f'R${valor_reais} convertidos para dólar valem USD${valor_reais/cotação:.2f}')
