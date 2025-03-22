class ContaBancaria:
    def __init__(self, titular):
        # Inicializando os atributos da conta bancária
        self.titular = titular
        self.saldo = 0
        self.operacoes = []
    
    def depositar(self, valor):
        # Realiza o depósito, somando ao saldo
        self.saldo += valor
        self.operacoes.append(f"+{valor}")
    
    def sacar(self, valor):
        # Verifica se há saldo suficiente para o saque
        if self.saldo + valor >= 0:
            self.saldo += valor
            self.operacoes.append(f"{valor}")
        else:
            self.operacoes.append("Saque não permitido")
    
    def extrato(self):
        # Exibe as operações realizadas e o saldo final
        operacoes_formatadas = ", ".join(self.operacoes)
        print(f"Operações: {operacoes_formatadas}; Saldo: {self.saldo}")


# Leitura do nome do titular
nome_titular = input().strip()
conta = ContaBancaria(nome_titular)

# Leitura das transações
entrada_transacoes = input().strip()
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

# Processa cada transação
for valor in transacoes:
    if valor > 0:
        conta.depositar(valor)
    else:
        conta.sacar(valor)

# Exibe o extrato final
conta.extrato()
