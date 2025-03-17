saldo = 1000;
saque = 500;
# if ternário
status = "sucesso" if saldo >= saque else "insuficiente";
print(f"Saque efetuado com {status}");