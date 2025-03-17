opcao = int(input("Digite 1 para sacar, 2 depositar, 0 sair: "));
saldo = 0;

while opcao != 0:
    if opcao == 1:
        valor = float(input("Digite o valor do saque: "));
        saldo = saldo - valor;
    elif opcao == 2:
        valor = float(input("Digite o valor do deposito: "));
        saldo = saldo + valor;
    print("Saldo da conta: ", saldo);
    opcao = int(input("Digite 1 para sacar, 2 depositar, 0 sair: "));
print("Fim do programa");