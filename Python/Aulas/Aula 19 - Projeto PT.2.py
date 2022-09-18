import csv
import requests as r
import datetime as dt
url = 'http://api.covid19api.com/dayone/country/brazil'
resp = r.get(url)
final_data = []
CONFIRMADOS = 0
MORTES = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4

with open('brasil_covid_editado.csv', 'r+', encoding='utf-8') as projeto:
    reader = csv.reader(projeto)
    for linha in reader:
        final_data.append(linha)
#    print(final_data)

"""for i in range(0, len(final_data)):
    print(final_data[i])"""
for i in range(0, len(final_data)):  # É necessário que o final_data tenha até somente o 10 caractere
    final_data[i][DATA] = final_data[i][DATA][:10]

for i in range(1, len(final_data)):  # Aqui vamos transformar todas as datas em valores de datetime, exceto header
    final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA], '%Y-%m-%d')
    print(f'{final_data[i]}', end='\n')

"""AGORA VAMOS UTILIZAR UMA NOVA API PARA GERAR GRÁFICOS COM O PYTHON
                QUICK CHART - quickchart.io                                 
                
Sempre precisaremos informar qual o tipo de gráfico que estamos criando e também os dados que serão responsáveis pela
geração desse gráfico:
type: 'bar'
labels: são rótulos do eixo X
E o eixo Y será indicado por um label e os valores reais de dados.

{type:'bar',data:{labels:['Q1','Q2','Q3','Q4'], 
datasets:[{label:'Users',data:[50,60,70,180]}, 
{label:'Revenue',data:[100,200,300,400]}]}}"""

# Vamos criar algumas funções helpers para ajudar com a interação:
def get_datasets(y, labels):  # função responsável pelos datasets do eixo y. O Y pode conter 1 ou mais dados...
    if type(y[0]) == list:  #Primeira coisa é verificar se o tipo do primeiro valor de Y é uma lista ou valor comum
        datasets = []  # Se for uma lista... vamos inicializar essa variável contendo os valores de y e respectivos labels
        for i in range(len(y)):  # Para cada item vamos criar um dicionário contendo o label e os dados de Y
            datasets.append({
                'label': labels[i],  # Sempre na posição atual do item
                'data': y[i]  # Sempre na posição atual do item
            })
        return datasets
    else:
        return [  # se não for uma lista vamos retornar uma lista de um único valor de dicionário com um único label
            {
                'label': labels[0],  # Por isso é na posição 0, se trata do único valor
                'data': y  # e o Y é o unico dado disponível para aquele label
            }
        ]


def set_title(title=''):  # Função apenas para definir um título do gráfico, a str vazia é para caso não seja informado
    if title != '':  # Se o título for diferente de uma string vazia eu vou mostrar o título: o display é 'True'
        display = 'true'
    else:  # Caso o título seja uma string vazia eu não mostro nada: o display é 'False'
        display = 'false'  # A API exige que os valores true e false sejam escritos em minúsculo
    return {
        'title': title,
        'display': display
    }


def create_chart(x, y, labels, kind='bar', title=''):  # função que cria o dicionário que representa o gráfico.
    # Essa função precisa receber os dados de X e Y, os rótulos, o tipo de gráfico e o título.
    datasets = get_datasets(y, labels)  # são os dados de Y
    options = set_title(title)  # chave responsável pela definição do título

    chart = {  # O dicionário que define a representação do gráfico
        'type': kind,  # O tipo de gráfico
        'data': {  # Os dados, sendo:
            'labels': x,  # Os rótulos do eixo X
            'datasets': datasets  # Os rótulos do eixo Y
        },
        'options': options  # As opções do título
    }

    return chart  # Retornando o gráfico completo


# Construir uma função que faça a requisição lá na API utilizando esse dicionário:
def get_api_chart(chart):
    url_base = 'https://quickchart.io/chart'  # Apenas a url que será usada para acessar a API
    resp = r.get(f'{url_base}?c={str(chart)}')  # Verificando se a API está respondendo, sendo que C é apenas o ...
                                                # parâmetro utilizado e uma transformação do 'chart' para string
    return resp.content
""" Essa chamada da API vai retornar a imagem do gráfico, ou seja, o arquivo de imagem, para conseguirmos utilizar ela
ou até mesmo para guardarmos ela junto com o projeto, precisamos transformar para números binários de forma que o PC
consiga ler esses dados. 

Dessa forma precisamos retornar o CONTENT dessa imagem, que é um valor binário."""

def save_image(path, content):  # Função responsável por salvar essa imagem com dois parâmetros: O caminho do arquivo e
                                # o conteúdo do arquivo.
    with open(path, 'wb') as image:  # Sendo que aqui iremos escrever um valor binário por isso 'wb' com b de binário
        image.write(content)  # No arquivo image escreva o content... bem simples


"""Além de salvar a imagem aqui, vamos criar outra função para mostrar essa imagem aqui no computer. 
Para isso precisaremos importar duas bibliotecas..."""
from PIL import Image  # Biblioteca de imagens do Python
from IPython.display import display  # Biblioteca de display do Python

def display_image(path):  # Função que vai mostrar essa imagem, recebe o caminho do arquivo
    img_pil = Image.open(path)  # Função open desse módulo
    display(img_pil)


"""Agora sim iremos criar o gráfico da seguinte maneira: Será um plot de barras em grupos mostrando a evolução do nº
de casos confirmados e do nº de casos recuperados desse dataset. Serão 2 dados diferentes para Y, 1 - confirmados, 
2 - recuperados. Por uma questão de visualização lógica iremos contabilizar de 10 em 10 dias. """

y_data_1 = []
for obs in final_data[1::10]:  # Para cada obs nos dados finais iremos contabilizar, do 1, ignorando o header, até o fim
                               # pulando de 10 em 10 com o slice.
    y_data_1.append(obs[CONFIRMADOS])

y_data_2 = []
for obs in final_data[1::10]:  # A mesma coisa só que agora para os recuperados...
    y_data_2.append(obs[RECUPERADOS])

labels = ['Confirmados', 'Recuperados']
# Aqui são declarados os rótulos do gráfico, 'confirmados', 'recuperados'.

x = []  # Aqui faremos a mesma coisa com os dados de X
for obs in final_data[1::10]:  # Para cada observação faremos o plot dos dados com base nas DATAS
    x.append(obs[DATA].strftime('%d/%m/%Y'))
""" No entanto os valores de DATA estão em tempo e precisamos passar para string novamente. 
Nesse caso o strFtime passa de datetime para string o contrário é com P."""

chart = create_chart(x, [y_data_1, y_data_2], labels, title='Gráfico confirmados vs recuperados')
# Chart é o gráfico passando todos os parâmetros sendo que o Y é sempre uma lista
chart_content = get_api_chart(chart)
# Acessando o api gerador de gráficos
save_image('meu-primeiro-gráfico.png', chart_content)
# Salvando a imagem na mesma pasta, se quisesse salvar em pasta diferente deveria especificar o caminho
display_image('meu-primeiro-gráfico.png')
# Aqui seria para mostrar o gráfico, mas pelo visto não deu certo...

# Essa biblioteca também permite gerar QR CODES
from urllib.parse import quote
def get_api_qrcode(link):
    text = quote(link)  # parsing do link para url
    url_base = 'https://quickchart.io/qr'
    resp = r.get(f'{url_base}?text={text}')
    return resp.content

url_base = 'https://quickchart.io/chart'
link = f'{url_base}?c={str(chart)}'
save_image('qr-code.png', get_api_qrcode(link))
display_image('qr-code.png')

