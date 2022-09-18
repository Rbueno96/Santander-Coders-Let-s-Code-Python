import requests as r  # r é um apelido só para facilitar a menção durante o programa.
url = 'http://api.covid19api.com/dayone/country/brazil'
resp = r.get(url)
# print(resp.status_code)  # Se faz necessário manter o print aqui para mostrar se está ou não funcionando.

raw_data = resp.json()  # Aqui vamos guardar os dados de uma forma "CRUA" gerados pela troca de informações
                        #dentro de uma variável, sendo que essa API também utiliza o Json.

#print(raw_data[0], end='\n')  # Aqui o 0 é para apenas visualizarmos quais são os headers, ou o que está contido nesse
                                # primeiro ponto.
final_data = []
for obs in raw_data:
    final_data.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])
final_data.insert(0, ['Confirmados', 'Mortes', 'Recuperados', 'Ativos', 'Data'])
#print(final_data)
# Aqui vamos retirar o Timezone que não é uma informação pertinente para nós
# Vamos criar também algumas constantes para referenciar cada posição dentro da lista
CONFIRMADOS = 0
MORTES = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4
for i in range(0, len(final_data)):  #Aqui alterei o 1 pelo 0 para também mostrar o header
    final_data[i][DATA] = final_data[i][DATA][:10]  #Aqui o :10 é para manter até o 9º caracter que é o que interessa
#    print(f'{final_data[i]}', end='\n')  #[indice] para printar todos os indices e quebra de linha no parâmetro end.
# Vamos criar um csv com os dados que temos até o momento...
import csv
"""with open('brasil_covid.csv', 'w', encoding='utf-8', newline='') as projeto:
    writer = csv.writer(projeto)  # Aqui a gente chama o nome do que estamos escrevendo.
    writer.writerows(final_data)"""
# Agora vamos organizar a data e transformar em um datetime que será reconhecido pelo Python
import datetime as dt
"""# Só para conhecimento estas são as formas de transformação do datetime:
print(dt.time(15, 45, 21, 7), 'Hora:minuto:segundo:microsegundo')
print('-' * 10)
print(dt.date(2022, 09, 13), 'Ano-mês-dia')
print('-' * 10)
print(dt.datetime(2022, 09, 13, 15, 45, 21, 07), 'Ano-mês-dia Hora:minuto:segundo:microsegundo')

Uma das vantagens de se utilizar as datas com datetime é que é possível somar, subtrair datas e determinar dias, minutos
ou até segundos entre as datas.

natal = dt.date(2022, 12, 25)
reveillon = dt.date(2023, 1, 1)
print(reveillon - natal)
print((reveillon - natal).days)
print((reveillon - natal).seconds)
print((reveillon - natal).microseconds)"""

for i in range(1, len(final_data)):  # Aqui vamos transformar todas as datas em valores de datetime, exceto header
    final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA], '%Y-%m-%d')  # Passando parâmetro de config da data
    # Essa função strptime transforma de str p/ time
#    print(f'{final_data[i]}', end='\n')  # Vou manter a outra forma de exibição das datas, acho melhor visualmente.

with open('brasil_covid_editado.csv', 'w', encoding='utf-8', newline='') as projeto:
#    print(final_data)
    writer = csv.writer(projeto)  # Aqui a gente chama o nome do que estamos escrevendo.
    writer.writerows(final_data)

#print(final_data)