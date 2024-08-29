# lista_doces = []

# while len(lista_doces) < 5: # o 'len' pega o tamanho da lista
    #doce = input('Digite um doce: ')
    #lista_doces.append(doce)

#print('Lista de doces:', lista_doces)

lista = []

lista.append(150)
lista.append(250)
lista.append(350)

print('lista após adição:', lista)

lista.remove(250)
print('lista depois da remoção:', lista)

del lista[0]
print('lista depois do del:', lista)

lista.insert(0, 100)
print('lista depois do insert:', lista)

elementoremovido = lista.pop()
print('lista depois do pop:', lista)
print('o elemento removido com pop foi ', elementoremovido)
