def calcular_saldo(transacoes):
    saldo = 0

    # Itera sobre cada transação na lista e adiciona o valor ao saldo
    for transacao in transacoes:
      print(saldo,transacao)
      saldo += float(transacao) 

    # Retorna o saldo formatado como moeda brasileira com a saída conforme o exemplo
    return f"Saldo: R$ {saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


# Converte os valores de string para float
transacoes = [100, -50, 200]

# Calcula o saldo com base nas transações informadas
resultado = calcular_saldo(transacoes)

# Exibe o resultado
print(resultado)
# https://markdownlivepreview.com/
# Lógica Simplificada: Removi a distinção entre transações positivas e negativas, pois o operador += já cobre ambos os casos. O valor negativo subtraí automaticamente do saldo.
# Resultado Formatado: Mantive a formatação de saída para mostrar o saldo de forma adequada.