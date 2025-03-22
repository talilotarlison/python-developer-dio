# importe datetime
# https://docs.python.org/pt-br/3.13/tutorial/classes.html
from datetime import datetime
#https://cursos.alura.com.br/forum/topico-duvida-private-nos-atributos-267898
# funcao pega hora e data do sistema
def get_data_hora():
    data_e_hora_atuais = datetime.now()
    return data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")

# funcao status
def get_status():
    return { "SUCESSO" : True, "ERROR":False}

# class banco 
class Banco:
    def __init__(self,nome_banco:str,cnpj:str):
        self.nome_banco = nome_banco
        self.cnpj = cnpj
        self.contas = []
        self.__logs = []
  
    def adicionar_conta(self, conta:object):
        status = get_status()
        
        nova_conta = None
        
        if(len(self.contas))== 0:
          nova_conta = status["SUCESSO"]
        else:
          for conta_arquivada in self.contas:
            if conta_arquivada.cpf == conta.cpf:
              # print(conta_arquivada, "CONTA JA EXITE NO SISTEMA")
              nova_conta = status["ERROR"]
            else:
              nova_conta = status["SUCESSO"]
              # print("CONTA NÃO EXITE NO SISTEMA")

          
        if nova_conta: 
            self.contas.append(conta)
            self.__set_log(conta=conta.cpf, status=status["SUCESSO"])
            print("Conta Criada com Sucesso")
        else:
            self.__set_log(conta=conta.cpf, status=status["ERROR"])
            print("Erro ao Criar, conta ja existe no sistema")
            
            
    def __set_log(self, conta:str, status:bool=True):
        data_e_hora = get_data_hora()
        
        if status:
          log_sucesso = f"Conta {conta} criada com sucesso as {data_e_hora}"
          self.__logs.append(log_sucesso)
        else :
          log_erro = f"Conta {conta} já existe , error ao criar conta as {data_e_hora}"
          self.__logs.append(log_erro)

    def get_logs(self):
      for log in self.__logs:
        print(log)

    def get_contas(self):
      for conta in self.contas:
        print(f"Nome: {conta.nome}\n Tipo : {conta.tipo_conta}\n Numero : {conta.num_conta}\n Digito: {conta.digito}\n Saldo: R$ {conta.saldo:.2f}")
    
    def get_dados_banco(self):
      print(f"Nome Banco: {self.nome_banco}")
      print(f"CNPJ Banco: {self.cnpj}\n")
    
    def get_num_contas(self):
      return len(self.contas)
      
# class cliente
class Cliente:
    def __init__(self,nome:str,cpf:str,tipo_conta:str,digito:int):
        self.saldo = 50 if tipo_conta == "Corrente" else 0
        self.__logs = []
        self.nome = nome
        self.cpf = cpf
        self.tipo_conta = tipo_conta
        self.num_conta = "0001"
        self.digito = digito + 1
    
    def depositar(self, valor):
      status = get_status()
      
      LIMITE_DEPOSITO = 1000
      
      if valor <= LIMITE_DEPOSITO:
        self.saldo += valor
        print(f"Deposito de R$ {valor:.2f} feito com sucesso!")
        self.__set_log(tipo="Deposito", valor=valor, status=status["SUCESSO"])
      else:
         print(f"Deposito de R$ {valor:.2f} maior que o limite R$ {LIMITE_DEPOSITO:.2f} permitido")
         self.__set_log(tipo="Deposito",valor=valor, status=status["ERROR"])
      
    def sacar(self, valor):
      status = get_status()
       
      LIMITE_SAQUE = 500
      
      if self.saldo >= valor:
        if valor <= LIMITE_SAQUE:
          self.saldo -= valor
          print(f"Saque de R$ {valor:.2f} feito com sucesso!")
          print(f"Saldo atual: R$ {self.saldo:.2f}")
          self.__set_log(tipo="Saque",valor=valor, status=status["SUCESSO"])
        else:
          print(f"Saque de R$ {valor} maior que o limite R$ {LIMITE_SAQUE:.2f} permitido!")
          print(f"Saldo atual: R$ {self.saldo:.2f}")
          self.__set_log(tipo="Saque",valor=valor, status=status["ERROR"])
      else:
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print(f"Saldo insuficiente não pode sacar R$ { valor:.2f}")
        self.__set_log(tipo="Saque",valor=valor, status=status["ERROR"])
    
    def get_logs(self):
        for log in self.__logs:
          print(log)

    def __set_log(self, tipo:str,valor:float ,status:bool=True):
        data_e_hora = get_data_hora()
        
        if status:
          log_sucesso = f"{tipo} de {valor} realizado com sucesso as {data_e_hora}"
          self.__logs.append(log_sucesso)
        else :
          log_erro = f"{tipo}  de {valor} invalido, error na transação as {data_e_hora}"
          self.__logs.append(log_erro)

# instancia da class Banco    
b = Banco(nome_banco='Nubank',cnpj="156456465")
 
b.get_logs()
b.get_dados_banco()

print(b.get_num_contas())

# instancia da class Cliente    
c = Cliente(nome="Joao",cpf="154579",tipo_conta="Poupanca", digito=b.get_num_contas())

b.adicionar_conta(c)
b.get_contas()

print(b.get_num_contas())
c.get_logs()

# instancia da class Cliente   
c1 = Cliente("Kaio","154778","Corrente", b.get_num_contas())
b.adicionar_conta(c1)
b.get_contas()

c1.depositar(1000)
c1.sacar(500)
c1.get_logs()

print(b.get_num_contas())
b.get_logs()

b.get_contas()

# instancia da class Cliente   
c3 = Cliente("Kaio","154778","Corrente", b.get_num_contas())
b.adicionar_conta(c3)
b.get_contas()
b.get_logs()

b.get_contas()
