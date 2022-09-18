# Manipulando arquivos com o Python

# def open é preciso passar 2 parâmetros
# FORMAS DE LEITURA DE UM ARQUIVO 'READ'
# arquivo = open('Caminho do arquivo', 'Modo de abertura sendo "r" para leitura')
"""arquivo = open('Aula 15 - TESTE.txt', 'r', encoding='utf-8')  # O encoding é necessário para visualizarmos os acentos
texto = arquivo.read()
print(texto)
# É necessário sempre fechar a conexão com o arquivo também...
arquivo.close()"""

"""# Outras formas de acessar o texto e linha por linha:
# Utilizando o while:
arquivo = open('Aula 15 - TESTE.txt', 'r', encoding='utf-8')
linha = arquivo.readline()
while linha != '':  # Enquanto a linha for diferente de um espaço vazio '' faça
    print('\033[33m', linha, end='' '\033[m')
    linha = arquivo.readline()
arquivo.close()"""

"""# Outras formas de acessar o texto e linha por linha:
# Utilizando o for:
arquivo = open('Aula 15 - TESTE.txt', 'r', encoding='utf-8')
for linha in arquivo:
    print('\033[34m', linha, end='' '\033[m')
arquivo.close()"""

# Outras formas de acessar o texto e linha por linha:
# Utilizando o with:
"""with open('Aula 15 - TESTE.txt', 'r', encoding='utf-8') as arquivo:  # Dessa forma abro temporariamente o arquivo e dou
    # um apelido pra ele "arquivo"
    texto = arquivo.read()
    print(texto)"""
# Nesse caso não preciso me preocupar em fechar o arquivo, ele já está fechado fora do 'with'.

# MODO DE ESCRITA DE UM ARQUIVO: BASICAMENTE DUAS MANEIRAS, ARQUIVO NOVO OU ADIÇÃO DE TEXTO A UM ARQUIVO EXISTENTE
# Modo de escrita 'WRITE':
"""with open('arquivo_teste.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Essa é a primeira linha de teste que escrevi utilizando o Python\n')
    arquivo.write('Essa é a segunda linha de teste que escrevi utilizando o Python\n')
with open('arquivo_teste.txt', 'r', encoding='utf-8') as arquivo:
    print(arquivo.read())
# Modo de adição 'ADD':
with open('arquivo_teste.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('Essa é a terceira linha de teste que escrevi utilizando o Python\n')
with open('arquivo_teste.txt', 'r', encoding='utf-8') as arquivo:
    print(arquivo.read())"""  # OS MODOS DE READ, WRITE E ADD DEVEM SER RESPEITADOS, CASO CONTRÁRIO RETORNARÁ UM ERRO
# R+ permite a utilização de todos os modos ao mesmo tempo

"""with open('arquivo_teste.txt', 'r+', encoding='utf-8') as arquivo:
    arquivo.write('Essa é a quarta linha de teste que escrevi utilizando o Python\n')
    print(arquivo.read())"""

# Novos testes por conta própria agora:
with open('arquivo_teste2.txt', 'w', encoding='utf-8') as teste:
    teste.write('1ª Linha de texto')
    teste.write(' 2ª Linha de texto sem colocar a quebra de linha contrabarra n')  #Se eu não colocar a quebra de linha
    #mesmo sendo numa outra função, vai ficar colado na anterior. Então é necessário utilizar o contrabarra N
    teste.write('\n2ª Linha de texto com contrabarra')

#Agora vamos fazer o teste com o Add:
with open('arquivo_teste2.txt', 'a', encoding='utf-8') as teste:
    teste.write('\n3ª Linha de texto pensando em não substituir as anteriores')  #Ok, deu certo

#Agora vamos testar com o Write novamente, sem colocar as anteriores verificando se haverá substituição:
"""with open('arquivo_teste2.txt', 'w', encoding='utf-8') as teste:
    teste.write('\n4ª Linha de texto pensando em não substituir as anteriores')  #Não deu certo. Se eu utilizar o Write
    #depois de já ter escrito, ele vai substituir e eu perderei o texto anterior... Então, uma vez escrito, somente
    #utilizar o Add."""
#    print(teste.read())  # Não é possível ler pq está em modo de escrita...

with open('arquivo_teste2.txt', 'r+', encoding='utf-8') as teste:
    print(teste.read())  # CONSIGO LER E PRINTAR
    teste.write('\n5ª Linha de texto sem substituir as anteriores')  #CONSIGO ESCREVER NO ARQUIVO
    print(teste.read())  # POR QUE NÃO CONSIGO LER NOVAMENTE COM O VALOR INSERIDO????
    teste.readable()
    print(teste.read())