import os
'''
FOR é um laço de repetição que tem um nº de iterações "fixas",
ou seja, quando sabemos o número que temos que iterar. Usamos o
FOR para ler listas, tuplas, mapas e dicionários no Python.

Exemplo:

FOR elemento in sequencia
    faça algo com o elemento


LISTA: é uma estrutura de dados que é delimitado por colchetes "[ ]", 
colocamos dentro dos colchetes qualquer tipo de dado:
- string (texto) ex. ['avocados', 'from', 'mexico', 'linux supremacy']
- int (valor numérico inteiro) ex. [34, 43, 23, 540]
- float (valor numérico com decimais) ex. [0.50, 4.30, 32.42]
- boolean (valor binário, verdadeiro ou falso, 0 ou 1) ex. [True, False, True, False]

PEGADINHA: A lista é mutável
'''

frutas = ['laranja', 'banana', 'maçã', 'melancia']
# print(frutas[0])
# print(frutas[1])
# print(frutas[2])
# print(frutas[3])
# print(frutas[8]) - erro de índice
# print(frutas[-1]) # pega o último item da lista


''' Métodos da Lista

.apend()  -  ele insere no final da lista, ele "apenda"
.pop() - remove da lista o último item da lista quando ele não é específico
também pode colocar um valor int para ser removido da lista
'''

# print(frutas)
# frutas.pop()
# print(frutas)

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir, [a]pagar, [l]istar')

    if opcao  == 'i':
        os.system
