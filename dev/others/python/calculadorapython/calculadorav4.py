print('Calculadora Python v4')

continuar = True
while continuar == True:
    operacao = int(input('Qual operação deseja realizar? (1 = adição; 2 = subtração; 3 = multiplicação; 4 = divisão; 5 = potenciação) '))
    while 0 < operacao < 6:
        num1 = float(input('Digite um número. '))
        num2 = float(input('Digite outro número. '))
        break
    if operacao == 1:
        resultado = num1 + num2
    elif operacao == 2:
        resultado = num1 - num2
    elif operacao == 3:
        resultado = num1 * num2
    elif operacao == 4:
        resultado = num1 / num2
    elif operacao == 5:
        resultado == num1 ** num2
    else:
        print('Perdão, mas você precisa escolher uma operação entre 1 e 5.')
    while 0 < operacao < 6:
        print(f'O resultado da operação é {resultado}')
        break
    continuarsn = input('Deseja continuar? (s/n) ')
    if continuarsn == 's' or continuar == 'S':
        continuar = True
    else:
        continuar = False
        break
exit()
