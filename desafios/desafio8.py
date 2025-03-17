# Desafio 2

def filtrar_transacoes(transacoes, limite):
    transacoes_filtradas = []

    # TODO: Itere sobre cada transação na lista:
    # TODO: Verifique se o valor absoluto da transação é maior que o limite:
    # TODO: Adicione a transação à lista filtrada:
    # TODO retornar a lista filtrada
    for transacao in transacoes:
        if abs(transacao) > limite:
            transacoes_filtradas.append(transacao)
    return transacoes_filtradas
       
        
transacoes = [[100, -50, 300, -150], 100]	#Transações: [300, -150]

# TODO: Filtre as transações que ultrapassam o limite:
resultado = filtrar_transacoes(transacoes[0], transacoes[1])
print(f"Transações: {resultado}")