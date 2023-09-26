# Importa as bibliotecas necessárias
import datetime

# Define uma função para receber as contas a pagar
def receber_contas():
    # Cria uma lista para armazenar as contas
    contas = []

    # Solicita ao usuário as informações sobre as contas
    while True:
        # Solicita o nome da conta
        nome = input("Nome da conta: ")

        # Solicita o valor da conta
        valor = float(input("Valor da conta: "))

        # Solicita a data de vencimento da conta
        vencimento = input("Data de vencimento (dd/mm/aaaa): ")

        # Converte a data de vencimento para um objeto datetime
        vencimento = datetime.datetime.strptime(vencimento, "%d/%m/%Y")

        # Adiciona a conta à lista
        contas.append({
            "nome": nome,
            "valor": valor,
            "vencimento": vencimento
        })

        # Solicita ao usuário se ele deseja continuar adicionando contas
        continuar = input("Deseja continuar adicionando contas? (s/n): ")

        if continuar != "s":
            break

    return contas

# Define uma função para receber o valor que será recebido
def receber_dinheiro():
    # Solicita ao usuário o valor que será recebido
    return float(input("Quanto você vai receber neste mês? "))

# Define uma função para calcular o saldo final
def calcular_saldo_final(contas, dinheiro):
    # Calcula o total de contas a pagar
    total_contas = 0
    for conta in contas:
        total_contas += conta["valor"]

    # Calcula o saldo final
    saldo_final = dinheiro - total_contas

    return saldo_final

# Recebe as contas a pagar
contas = receber_contas()

# Recebe o valor que será recebido
dinheiro = receber_dinheiro()

# Calcula o saldo final
saldo_final = calcular_saldo_final(contas, dinheiro)

# Imprime o saldo final
print("O seu saldo final é de R$%.2f" % saldo_final)
