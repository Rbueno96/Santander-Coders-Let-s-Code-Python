# Modos de leitura de um CSV:
# Importando a biblioteca chamada CSV:
"""import csv
with open('Aula 16 - TESTE.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)  # Criação de um leitor com a biblioteca CSV.reader e chamando o apelido do file
#    header = next(leitor)  # Função para ignorar o cabeçalho
    for linha in leitor:
        print(linha)"""

# Sem necessidade de importar a biblioteca CSV:
import csv

"""with open('Aula 16 - TESTE.csv', 'r', encoding='utf-8') as csv_file:
    linhas = csv_file.read()
    linhas = linhas.split('\n')  # Esse split separa com quebra de linha para criar diferentes listas
    for linha in linhas:
        linha = linha.split(';')  # Esse split separa em cada linha de acordo com o ;
        print(linha)"""

# Modo de escrita de arquivos CSV:
"""with open('users.csv', 'w', encoding='utf-8', newline='') as arquivo_users:
    # OBS: É necessário passar o parâmetro newline='' para que ele não insira uma linha vazia à cada writerow
    escritor = csv.writer(arquivo_users)  # Cria uma variável para escrever o arquivo passando o apelido do file
    escritor.writerow(['nome', 'sobrenome', 'e-mail', 'genero'])
    escritor.writerow(['Rodrigo', 'Bueno', 'robueno1996@gmail.com', 'Masculino'])"""

# Exemplo: Programa de cadastro.
"""
header = ['nome', 'sobrenome']
dados = []
opt = input('O que deseja fazer?\n1 - Cadastrar\n0 - Sair\nDigite: ')
while opt != '0':
    nome = input('Qual é o seu nome? ')
    sobrenome = input('Qual é o seu sobrenome? ')
    dados.append([nome, sobrenome])
    opt = input('O que deseja fazer?\n1 - Cadastrar\n0 - Sair\nDigite: ')

# print(dados)

with open('users.csv', 'w', encoding='utf-8', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(header)
    writer.writerows(dados)  # Aqui tem o row está no plural para escrever várias linhas de uma vez

with open('users.csv', 'r', encoding='utf-8', newline='') as csv_reading:
    csv_reading = csv.reader(csv_reading, delimiter=',')
    for row in csv_reading:
        print(row)"""

with open('users.csv', 'r', encoding='utf-8') as leitura_csv:
    leitor = csv.reader(leitura_csv)
    for linha in leitor:
        if linha[0].lower() == 'rodrigo':  # Aqui consegui printar somente o meu nome utilizando o índice
            print(f'{linha}\n')

with open('users.csv', 'r', encoding='utf-8') as leitura_csv:
    leitor = csv.reader(leitura_csv)
    for linha in leitor:
        print(linha)
