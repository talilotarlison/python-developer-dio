MAIOR_IDADE = 18;

def maior_idade(idade):
    if idade >= MAIOR_IDADE:
        return True;
    else:
        return False;

idade = int(input("Digite a idade: "));
if maior_idade(idade):
    print("Maior de idade");
else:
    print("Menor de idade");

