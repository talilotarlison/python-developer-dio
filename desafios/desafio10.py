# Importe datetime
from datetime import datetime

# Funcao pega hora e data do sistema
class DateTime:

    def __init__(self):
        self.data_e_hora_atuais = datetime.now()
        self.data = self.data_e_hora_atuais.strftime("%d/%m/%Y")
        self.hora = self.data_e_hora_atuais.strftime("%H:%M")
        self.data_hora = self.data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")

    def get_data(self):
        return self.data

    def get_hora(self):
        return self.hora

    def get_data_hora(self):
        return self.data_hora

# Funcao status
class Status:

    def __init__(self):
        self.status = { "SUCESSO" : True, "ERROR":False}

    def get_status(self):
        return self.status

# Class banco => https://docs.python.org/pt-br/3.13/tutorial/classes.html
class Banco:

    def __init__(self,nome_banco:str,cnpj:str):
        self.nome_banco = nome_banco
        self.cnpj = cnpj
        self.tipo_conta = { "1" : "Poupança", "2":"Corrente"}
        self.contas = []
        self.__logs = []
  
    def adicionar_conta(self, conta:object):
        status = Status().get_status()
        
        nova_conta = None
        
        if(len(self.contas))== 0:
          nova_conta = status["SUCESSO"]
        else:
          for conta_arquivada in self.contas:
            if conta_arquivada.cpf == conta.cpf:
              # print(conta_arquivada, "CONTA JA EXISTE NO SISTEMA")
              nova_conta = status["ERROR"]
            else:
              nova_conta = status["SUCESSO"]
              # print("CONTA NÃO EXISTE NO SISTEMA")
      
        if nova_conta: 
            self.contas.append(conta)
            self.__set_log(conta=conta.cpf, status=status["SUCESSO"])
            print("Conta Criada com Sucesso")
        else:
            self.__set_log(conta=conta.cpf, status=status["ERROR"])
            print("Erro ao Criar, conta ja existe no sistema")
            
            
    def __set_log(self, conta:str, status:bool=True):
        data_e_hora = DateTime().get_data_hora()
        
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
        print(f"Nome: {conta.nome}\n Tipo : {conta.tipo_conta}\n Numero : {conta.num_conta}\n Agencia: {conta.digito}\n Saldo: R$ {conta.saldo:.2f}")
    
    def get_dados_banco(self):
      print(f"Nome Banco: {self.nome_banco}")
      print(f"CNPJ Banco: {self.cnpj}\n")
    
    def get_num_contas(self):
      return len(self.contas)

    def get_tipo_conta(self):
        return self.tipo_conta
    
    def get_conta_usuario(self, cpf:str):
        for conta_user in self.contas:
            if conta_user.cpf == cpf:
                return conta_user

# Class cliente
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
      status = Status().get_status()
      
      LIMITE_DEPOSITO = 1000
      
      if valor <= LIMITE_DEPOSITO:
        self.saldo += valor
        print(f"Deposito de R$ {valor:.2f} feito com sucesso!")
        self.__set_log(tipo="Deposito", valor=valor, status=status["SUCESSO"])
      else:
         print(f"Deposito de R$ {valor:.2f} maior que o limite R$ {LIMITE_DEPOSITO:.2f} permitido")
         self.__set_log(tipo="Deposito",valor=valor, status=status["ERROR"])
      
    def sacar(self, valor):
      status = Status().get_status()
       
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
        print(f"Saldo insuficiente, não pode sacar R$ { valor:.2f}")
        self.__set_log(tipo="Saque",valor=valor, status=status["ERROR"])
    
    def get_logs(self):
        for log in self.__logs:
          print(log)

    # Metodo privado  => https://cursos.alura.com.br/forum/topico-duvida-private-nos-atributos-267898
    def __set_log(self, tipo:str,valor:float ,status:bool=True):
        data_e_hora = DateTime().get_data_hora()
        
        if status:
          log_sucesso = f"{tipo} de {valor} realizado com sucesso as {data_e_hora}"
          self.__logs.append(log_sucesso)
        else :
          log_erro = f"{tipo}  de {valor} invalido, error na transação as {data_e_hora}"
          self.__logs.append(log_erro)

# Instancia da class Banco python    
banco_python = Banco(nome_banco='Python',cnpj="156456465")
 
# Welcome message
def welcome_message():
    print("#" * 30)
    print("Bem-vindo ao Banco Python")
    print("#" * 30)
    return 0

# printe line message
def print_line():
    print("#" * 30)
    return 0

# Depositar cliente
def depositar():
    valor = float(input("Digite o valor do depósito: "))
    cpf_usuario = input("Digite o CPF titular: ")
    has_user = banco_python.get_conta_usuario(cpf=cpf_usuario)
    if has_user:
        has_user.depositar(valor)
        print_line()
        cliente()
    else:
        print_line()
        print("Usuário não encontrado, tenta novamente")
        print_line()
        cliente()
    return 0

# Sacar cliente
def sacar():
    valor = float(input("Digite o valor do saque: "))
    cpf_usuario = input("Digite o CPF titular: ")
    has_user = banco_python.get_conta_usuario(cpf=cpf_usuario)
    if has_user:
        has_user.sacar(valor)
        print_line()
        cliente()
    else:
        print_line()
        print("Usuário não encontrado, tenta novamente")
        print_line()
        cliente()
    return 0

# Extract cliente
def extrato():
    cpf_usuario = input("Digite o CPF titular: ")
    has_user = banco_python.get_conta_usuario(cpf=cpf_usuario)
    if has_user:
        print(f"Titular: {has_user.nome}")
        print(f"Saldo: R$ {has_user.saldo:.2f}")
        print(f"Número da conta: {has_user.num_conta}")
        print(f"Agência: {has_user.digito}")
        print_line()
        print("Transações:")
        has_user.get_logs()
        print_line()
        cliente()
    else:
        print_line()
        print("Usuário não encontrado, tenta novamente")
        print_line()
        cliente()
    return 0

# Menu de açoes cliente
def menu_cliente():
    welcome_message()
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Ajuda")
    print("5 - Inicio")
    print("6 - Sair")
    print_line()
    return 0
# Menu de acoes clientes    
def cliente():
    menu_cliente()
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        depositar()
    elif opcao == 2:
        sacar()
    elif opcao == 3:
        extrato()
    elif opcao == 4:
        ajuda_cliente()
    elif opcao == 5:
        main()
    elif opcao == 6:
        exit()
    else:
        print_line()
        print("Opção inválida, tente novamente")
        print_line()
        cliente()
    return 0

# Funcao de ajuda cliente
def ajuda_cliente():
    welcome_message()
    print("Para realizar um depósito, digite 1")
    print("Para realizar um saque, digite 2")
    print("Para ver o extrato, digite 3")
    print("Para ajuda, digite 4")
    print("Para sair, digite 5")
    print_line()
    cliente()
    return 0


# Menu de acoes administracao
def cadastrar_conta():
    nome = input("Digite o nome do titular: ")
    cpf = input("Digite o CPF do titular: ")
    tipo_conta = input("Digite o tipo de conta: [1]Poupanca [2]Corrente: ")
    get_tipo_contas = banco_python.get_tipo_conta()
    if tipo_conta == "1":
        tipo_conta = get_tipo_contas["1"]
    elif tipo_conta == "2":
        tipo_conta = get_tipo_contas["2"]
    else:
        print_line()
        print("Opção inválida,tente novamente")
        print_line()
        cadastrar_conta()
    # Instancia da class Cliente  
    digito = banco_python.get_num_contas()
    cliente = Cliente(nome=nome,cpf=cpf,tipo_conta=tipo_conta,digito=digito)
    banco_python.adicionar_conta(cliente)
    main()
    return 0

# Listar contas
def listar_contas():
    banco_python.get_contas()
    main()
    return 0

# Logs contas
def logs_contas():
    banco_python.get_logs()
    main()
    return 0

# Menu ajuda admin
def ajuda_admin():
    welcome_message()
    print("Para cadastrar uma conta, digite 1")
    print("Para listar contas, digite 2")
    print("Para ver logs do sistema, digite 3")
    print("Para ajuda, digite 4")
    print("Para sair, digite 5")
    print_line()
    administracao()
    return 0

# Menu de acoes admistração
def menu_adm():
    welcome_message()
    print("1 - Cadastrar conta")
    print("2 - Listar contas")
    print("3 - Logs do sistema")
    print("4 - Ajuda")
    print("5 - Inicio")
    print("6 - Sair")
    print_line()
    return 0

# Menu de acoes clientes    
def administracao():
    menu_adm()
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        cadastrar_conta()
    elif opcao == 2:
        listar_contas()
    elif opcao == 3:
        logs_contas()
    elif opcao == 4:
        ajuda_admin()
    elif opcao == 5:
        main()
    elif opcao == 6:
        exit()
    else:
        print_line()
        print("Opção inválida, tente novamente")
        print_line()
        administracao()
    return 0

# Ajuda geral
def ajuda():
    welcome_message()
    print("Para acessar a administração, digite 1")
    print("Para acessar como cliente, digite 2")
    print("Para ajuda, digite 3")
    print("Para sair, digite 4")
    print_line()
    main()
    return 0

# Menu principal
def menu(): 
    welcome_message()
    print("1 - Administração")
    print("2 - Cliente")
    print("3 - Ajuda")
    print("4 - Sair")
    print_line()
    return 0

# Funcao principal main
def main():
    menu()
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        administracao()
    elif opcao == 2:
        cliente()
    elif opcao == 3:
        ajuda()
    elif opcao == 4:
        exit()
    else:
        print_line()
        print("Opção inválida, tenta novamente")
        print_line()
        main()
        return 0

# Start do programa
if __name__ == '__main__':
    main()
