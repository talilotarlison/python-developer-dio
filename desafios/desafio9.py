# EXERCÍCIO 02

def filtrar_transacoes(transacoes, limite):  # Função para filtrar transações que ultrapassam um determinado limite
    transacoes_filtradas = []  # Inicializa uma lista vazia para armazenar as transações filtradas
    for transacao in transacoes:  # Percorre todas as transações informadas
        if abs(transacao) > limite:  # Verifica se o valor absoluto da transação é maior que o limite
            transacoes_filtradas.append(transacao)  # Adiciona a transação à lista filtrada
    return [transacao for transacao in transacoes if abs(transacao) > limite]  # Retorna uma lista de transações filtradas usando list comprehension

entrada = input()  # Captura a entrada do usuário no formato "[valores], limite"

entrada_transacoes, limite = entrada.split("],")  # Divide a entrada em duas partes: a lista de transações e o limite
entrada_transacoes = entrada_transacoes.strip("[").replace(" ", "")  # Remove colchetes e espaços extras da entrada das transações
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]  # Converte a string processada em uma lista de números inteiros
limite = int(limite.strip())  # Converte o limite para inteiro
resultado = filtrar_transacoes(transacoes, limite)  # Aplica a função para filtrar as transações que ultrapassam o limite

print(f"Transações: {resultado}")
