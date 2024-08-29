from math import sqrt

class calculadora:
    def __init__(self):
        self.valorinicial = 0
        self.valoroperacao = 0
        self.operacao = 0
    
    def adicao(self):
        return self.valorinicial + self.valoroperacao
    
    def subtracao(self):
        return self.valorinicial - self.valoroperacao
    
    def multiplicacao(self):
        return self.valorinicial * self.valoroperacao
    
    def divisao(self):
        return self.valorinicial / self.valoroperacao

    def exponenciacao(self):
        return self.valorinicial ^ self.valoroperacao
    
    def raiz(self):
        return sqrt(valorinicial)

    def reset(self):
        self.valorinicial = 0
        self.operacao = 0

calc = calculadora()
print('Calculadora Python v5')

while True:
    print(calc.valorinicial)
    print('1 = adicao / 2 = subtracao')
    print('3 = multiplicacao / 4 = divisao')
    print('5 = exponenciacao / 6 = raiz quadrada')
    print('0 = limpar / outro numero = sair ')
    calc.operacao = int(input('O que deseja fazer? '))
    if calc.operacao == 0:
        calc.reset()
    if calc.operacao == 1:
        if calc.valorinicial == 0:
            calc.valorinicial = int(input('Digite o primeiro número: '))
        calc.valoroperacao = int(input('Digite o segundo número: '))
        calc.valorinicial = calc.adicao()
    if calc.operacao == 2:
        if calc.valorinicial == 0:
            calc.valorinicial = int(input('Digite o primeiro número: '))
        calc.valoroperacao = int(input('Digite o segundo número: '))
        calc.valorinicial = calc.subtracao()
    if calc.operacao == 3:
        if calc.valorinicial == 0:
            calc.valorinicial = int(input('Digite o primeiro número: '))
        calc.valoroperacao = int(input('Digite o segundo número: '))
        calc.valorinicial = calc.multiplicacao()
    if calc.operacao == 4:
        if calc.valorinicial == 0:
            calc.valorinicial = int(input('Digite o primeiro número: '))
        calc.valoroperacao = int(input('Digite o segundo número: '))
        calc.valorinicial = calc.divisao()
    if calc.operacao == 5:
        if calc.valorinicial == 0:
            calc.valorinicial = int(input('Digite o primeiro número: '))
        calc.valoroperacao = int(input('Digite o segundo número: '))
        calc.valorinicial = calc.exponenciacao()
    if calc.operacao == 6:
        if calc.valorinicial == 0:
            calc.valorinicial = int(input('Digite o número: '))
        calc.valorinicial = calc.raiz()
    if calc.operacao < 0 or calc.operacao > 6:
        break