class CaixaEletronico:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def verificar_saldo(self):
        return self.saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} realizado com sucesso."
        else:
            return "Valor inválido. O valor do depósito deve ser maior que zero."

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso."
        elif valor <= 0:
            return "Valor inválido. O valor do saque deve ser maior que zero."
        else:
            return "Saldo insuficiente."

# Função principal
def main():
    saldo_inicial = float(input("Digite o saldo inicial da conta: "))
    caixa = CaixaEletronico(saldo_inicial)

    while True:
        print("\n=== Caixa Eletrônico ===")
        print("1. Verificar Saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Sair")

        opcao = input("Escolha uma opção (1/2/3/4): ")

        if opcao == "1":
            print(f"Saldo atual: R${caixa.verificar_saldo():.2f}")
        elif opcao == "2":
            valor_deposito = float(input("Digite o valor a ser depositado: "))
            print(caixa.depositar(valor_deposito))
        elif opcao == "3":
            valor_saque = float(input("Digite o valor a ser sacado: "))
            print(caixa.sacar(valor_saque))
        elif opcao == "4":
            print("Obrigado por usar o Caixa Eletrônico. Volte sempre!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
