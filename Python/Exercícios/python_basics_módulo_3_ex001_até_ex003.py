"""Ex001 - Neste exercício você deve criar um programa que abra o arquivo
"alunos.csv" e imprima o conteúdo do arquivo linha a linha."""
import csv
copia = []
media = []
with open('alunos.csv', 'r', encoding='utf-8') as alunos:
    reader = csv.reader(alunos)
    for linha in reader:
        copia.append(linha)
        media.append(linha)

"""Ex002 - Para o segundo exercício, você deve criar um programa que realize uma 
cópia do arquivo "alunos.csv". Essa cópia deve ser um arquivo chamado 
"alunos_copia.csv"."""
with open('alunos-copia.csv', 'w', encoding='utf-8', newline='') as copy:
    writer = csv.writer(copy)
    writer.writerows(copia)

"""Ex003 - Finalmente chegamos ao último exercício dessa sequência relacionada à 
manipulação de arquivos.

Neste exercício você deve criar um novo arquivo chamado "alunos_media.csv". Esse novo arquivo é uma cópia de 
"alunos.csv" porém com uma coluna a mais chamada "Média" que vai abrigar os valores das médias das provas de cada 
aluno da lista."""

with open('alunos-media.csv', 'w', encoding='utf-8', newline='') as medium:
    writer = csv.writer(medium)
    writer.writerows(media)

media[0].append('Media')
for k, v in enumerate(media):  # Com enumerate consigo ignorar o cabeçalho utilizando as keys
    soma = 0  # Soma recebe 0 para não somar com o valor anterior
    if k > 0:  # Aqui ignoro o cabeçalho
        soma = (float(v[3]) + float(v[4]) + float(v[5]) + float(v[6])) / 4
        v.append(soma)  #Aqui o append foi apenas no V, e não em média. Pois é só no valor que vamos adicionar.
    print(f'{k}, {v}')

with open('alunos-media.csv', 'w', encoding='utf-8', newline='') as medium:
    writer = csv.writer(medium)
    writer.writerows(media)

"""for n in range(1, len(media)):  # Aqui consigo ignorar o cabeçalho
    for linha in media[n]:
        print(linha, end=' ')"""
"""soma = 0
    soma = (linha[3] + linha[4] + linha[5] + linha[6])/4
    media.append(soma)"""