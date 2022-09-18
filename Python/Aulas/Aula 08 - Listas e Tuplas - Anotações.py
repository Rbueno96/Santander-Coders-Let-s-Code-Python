"""Uma nova função das tuplas que até então eu não sabia é o unpacking...

Consiste em transformar os valores dentro de uma tupla em variáveis separadas

Dessa forma: """

nome_paises = ('Brasil', 'Argentina', 'Canadá', 'Japão', 'Chile')
b, a, ca, j, ch = nome_paises
print(ch, j)

# É possível também remover as vírgulas e trabalhar com os valores em strings com um * antes do nome da variável:
print(*nome_paises)
print(*f'{nome_paises}'.replace(', ', ' -> '))
print(f'{nome_paises}'.replace(', ', ' -> '))

# É possível também utilizar o