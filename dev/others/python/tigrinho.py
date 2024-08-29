import random
#codigo pelo tom
class TigrinhoDaSorte:
    def __init__(self):
        self.premio = 100
        self.saldo = 0

    def girar_roleta(self):
        return random.randint(0, 9)

    def depositar_dinheiro(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Você depositou {valor} reais. Saldo atual: {self.saldo} reais.")
        else:
            print("Valor de depósito inválido!")

    def jogar(self, aposta, numero):
        if aposta > self.saldo:
            print("Você não tem saldo suficiente para essa aposta!")
            return

        resultado = self.girar_roleta()
        print("O número sorteado foi:", resultado)

        if resultado == numero:
            premio_ganho = aposta * 10
            self.saldo += premio_ganho - aposta
            print("Parabéns! Você acertou o número e ganhou", premio_ganho, "reais!")
        else:
            self.saldo -= aposta
            print(f"Faz o L! Você perdeu R$ {aposta:.2f} kkkkkkk")

        print("Saldo atual:", self.saldo)

jogo = TigrinhoDaSorte()
print("Bem-vindo ao Tigrinho da Sorte!")

while True:
    print("\nMenu:")
    print("1. Depositar dinheiro")
    print("2. Jogar")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        valor_deposito = int(input("Digite o valor que deseja depositar: "))
        jogo.depositar_dinheiro(valor_deposito)
    elif opcao == '2':
        if jogo.saldo <= 0:
            print("Você ficou sem saldo. Por favor, deposite mais dinheiro.")
            continue
        aposta = int(input("Digite o valor da sua aposta: "))
        if aposta <= 0:
            print("A aposta deve ser maior que zero!")
            continue
        numero = int(input("Digite um número de 0 a 9 para apostar: "))
        if numero < 0 or numero > 9:
            print("Por favor, escolha um número entre 0 e 9!")
            continue
        jogo.jogar(aposta, numero)
    elif opcao == '3':
        print("Obrigado por jogar!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

