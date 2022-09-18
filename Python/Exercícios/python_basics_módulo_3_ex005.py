import requests
url = 'https://api.covid19api.com/country/brazil'
requisição = requests.get(url)
raw_data = requisição.json()
final_data = []
for obs in raw_data:
    final_data.append([obs['Confirmed'], obs['Date']])
CONFIRMADOS = 0
DATA = 1
for i in range(0, len(final_data)):
    final_data[i][DATA] = final_data[i][DATA][:10]
final_data.insert(0, ['Confirmados', 'Data'])
"""for linha in final_data:
    print(linha)"""
for k, v in enumerate(final_data):
    if k == 0:
        print(v)  # Se o k = 0, que é o cabeçalho, printa o v daquela linha, ou seja, o cabeçalho
    if k > 0:
        if int(v[0]) > 0:  # Se o int de confirmados = (v[0]) for maior do que zero, temos o primeiro caso de covid.
    #        print(k)  # Printei a key apenas para visualizarmos qual foi a linha, ou nesse caso, após quantos dias o Brasil
            # teve seu primeiro caso confirmado.
            print(f'{v}')  #E o v representa todos os values daquela linha.

print(f'O primeiro caso de Covid-19 confirmado no Brasil foi no dia 26 de fevereiro de 2020.')