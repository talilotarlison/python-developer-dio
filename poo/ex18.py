class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

class SistemaBancario:
    def __init__(self):
        self.contas = []
    
    def criar_conta(self, titular, saldo):
        self.contas.append(ContaBancaria(titular, saldo))
    
    def listar_contas(self):
        print(", ".join([f"{conta.titular}: R$ {conta.saldo}" for conta in self.contas]))

sistema = SistemaBancario()

while True:
    entrada = input().strip()
    if entrada.upper() == "FIM":  
        break
    titular, saldo = entrada.split(", ")
    sistema.criar_conta(titular, int(saldo))

sistema.listar_contas()
