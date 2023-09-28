class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.saldo_diario = 0  # Inicialmente, nenhum saque foi feito no dia
        self.saques_diarios = 0  # Inicialmente, nenhum saque foi feito no dia

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            return f'Depósito de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}'
        else:
            return 'Valor de depósito inválido.'

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo and self.saldo_diario + valor <= 500 and self.saques_diarios < 3:
            self.saldo -= valor
            self.saldo_diario += valor
            self.saques_diarios += 1
            return f'Saque de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}'
        elif self.saldo_diario + valor > 500:
            return 'Limite diário de saque excedido (R$500).'
        elif self.saques_diarios >= 3:
            return 'Você já fez 3 saques hoje. Limite de saques diários atingido.'
        else:
            return 'Saque não realizado. Saldo insuficiente ou valor inválido.'

    def extrato(self):
        return f'Saldo atual: R${self.saldo:.2f} - Saques diários: {self.saques_diarios} - Valor diário sacado: R${self.saldo_diario:.2f}'


def main():
    saldo_inicial = float(input('Informe o saldo inicial da conta: '))
    conta = ContaBancaria(saldo_inicial)

    while True:
        print('\nEscolha uma operação:')
        print('1 - Depósito')
        print('2 - Saque')
        print('3 - Extrato')
        print('4 - Sair')

        escolha = input('Digite o número da operação desejada: ')

        if escolha == '1':
            valor = float(input('Digite o valor do depósito: '))
            print(conta.deposito(valor))
        elif escolha == '2':
            valor = float(input('Digite o valor do saque: '))
            print(conta.saque(valor))
        elif escolha == '3':
            print(conta.extrato())
        elif escolha == '4':
            print('Saindo do banco. Até logo!')
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')


if __name__ == "__main__":
    main()
