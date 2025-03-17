from datetime import datetime
# conta de um unico usuario
# limite maximo de saque 500
# limite maximo de deposito 1000
# saldo inicial 0
# transacoes: deposito, saque, extrato

# funcao para pegar a data atual
# https://www.alura.com.br/artigos/lidando-com-datas-e-horarios-no-python
def data():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# dados da conta do usuario
conta = {
    "titular": "Lucas",
    "saldo": 0,
    "numero": "123-4",
    "agencia": "0001-1",
    "data_abertura": "10/08/2020",
    "transacoes": [],
}

# constante globais
LIMITE_SAQUE = 500
LIMITE_DEPOSITO = 1000

# menu de acoes
def menu():
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Ajuda")
    print("5 - Sair")

# funcao de deposito
def deposito():
    valor = float(input("Digite o valor do depósito: "))
    if valor > LIMITE_DEPOSITO:
        print("Valor acima do limite de depósito")
    else:
        conta["saldo"] += valor
        conta["transacoes"].append(f"Depósito de R$ {valor:.2f}, as {data()}")
        print("Depósito realizado com sucesso")

# funcao de saque
def saque():
    valor = float(input("Digite o valor do saque: "))
    if valor > LIMITE_SAQUE:
        print("Valor acima do limite de saque")
    elif valor > conta["saldo"]:
        print("Saldo insuficiente")
    else:
        conta["saldo"] -= valor
        conta["transacoes"].append(f"Saque de R$ {valor:.2f}, as {data()}")
        print("Saque realizado com sucesso")
# funcao de extrato
def extrato():
    print(f"Titular: {conta['titular']}")
    print(f"Saldo: R$ {conta['saldo']:.2f}")
    print(f"Número da conta: {conta['numero']}")
    print(f"Agência: {conta['agencia']}")
    print(f"Data de abertura: {conta['data_abertura']}")
    print("Transações:")
    for t in conta["transacoes"]:
        print(t)

# funcao de ajuda
def ajuda():
    print("Bem-vindo ao Banco Python")
    print("Para realizar um depósito, digite 1")
    print("Para realizar um saque, digite 2")
    print("Para ver o extrato, digite 3")
    print("Para ajuda, digite 4")
    print("Para sair, digite 5")
    
# funcao principal main
def main():
    while True:
        menu()
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            deposito()
        elif opcao == 2:
            saque()
        elif opcao == 3:
            extrato()
        elif opcao == 4:
            ajuda()
        elif opcao == 5:
            break
        else:
            print("Opção inválida")
# start do programa
main()
