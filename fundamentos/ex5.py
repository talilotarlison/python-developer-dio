MAIOR_IDADE = 18;
# verifica se a idade é maior ou igual a 18
def is_maior_idade(idade):
    if idade >= MAIOR_IDADE:
        return True;
    else:
        return False;
# pega a idade do usuário
def get_idade():
    return int(input("Digite a idade: "));
# mostra o status do usuário
def show_status():
    idade = get_idade();
    if is_maior_idade(idade):
        print("Maior de idade");
    else:
        print("Menor de idade");
# chama a função show_status
show_status();