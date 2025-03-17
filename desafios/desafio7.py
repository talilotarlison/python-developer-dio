def calcular_saldo(transacoes):
    saldo = 0

    # Itera sobre cada transação na lista e adiciona o valor ao saldo
    for transacao in transacoes:
      print(saldo,transacao)
      saldo += float(transacao) 

    # Retorna o saldo formatado como moeda brasileira com a saída conforme o exemplo
    return str(f"Saldo: R$ {saldo:,.2f}")


# Converte os valores de string para float
transacoes = [100, -50, 200]

# Calcula o saldo com base nas transações informadas
resultado = calcular_saldo(transacoes)

# Exibe o resultado
print(resultado)
