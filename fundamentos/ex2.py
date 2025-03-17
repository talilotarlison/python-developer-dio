def sacar(valor_saque:float, saldo:float):
  if saldo >= valor_saque:
    print("saque feito com sucesso");
  else:
    print("saldo insuficiente!");
  saldo_atual = saldo - valor_saque
  print("Saldo atual -> {}".format(saldo_atual)); 

sacar(43,79);

def deposito(valor_dep:float, saldo:float):
  saldo+= valor_dep;
  print("deposito feito com sucesso");
  print("Saldo atual -> {}".format(saldo)); 

deposito(43,79);