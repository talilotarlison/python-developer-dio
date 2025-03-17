conta_normal = true;
conta_universitaria = false;

saldo = 1000;
saque = 500;
# if aninhado
if conta_normal:
  if saldo >= saque:
    saldo = saldo - saque;
    print("Saque efetuado com sucesso");
    else:
      print("Saldo insuficiente");
elif conta_universitaria:
  if saldo >= saque:
    saldo = saldo - saque;
    print("Saque efetuado com sucesso");
    else:
      print("Saldo insuficiente");
else:
  print("Tipo de conta inválido");  