class Conta:
    def __init__(self, nome, valor, data_vencimento):
        self.nome = nome
        self.valor = valor
        self.data_vencimento = data_vencimento

def calcular_saldo(contas, renda_mensal):
    total_despesas = sum(conta.valor for conta in contas)
    saldo_disponivel = renda_mensal - total_despesas
    return saldo_disponivel

def main():
    contas = []

    # Adicione suas contas aqui
    contas.append(Conta("Aluguel", 350, "2023-10-05"))
    contas.append(Conta("jiu jitsu", 125, "2023-10-15"))
    contas.append(Conta("Internet", 170, "2023-10-20"))
    contas.append(Conta("Ana", 780, "2023-10-05"))
    contas.append(Conta("creedz", 1950, "2023-10-08"))
    contas.append(Conta("seguro", 100, "2023-10-25"))
    contas.append(Conta("DAS", 70, "2023-10-30"))
    contas.append(Conta("Nubank", 900, "2023-10-25"))

    renda_mensal = float(input("Informe sua renda mensal: "))

    saldo = calcular_saldo(contas, renda_mensal)

    print(f"Saldo disponível para o mês: R${saldo:.2f}")

if __name__ == "__main__":
    main()
