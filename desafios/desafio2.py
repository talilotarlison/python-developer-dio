def calular_impostos(salario:float, percentual:float):
    return salario * percentual/100

def percentual_impostos(salario:float):
    if salario <= 1100.00:
        return 5
    elif salario > 1100.01 and salario <= 2500.00:
        return 10
    else:
        return 15

def novo_salario_final(salario:float, beneficios:float):
    imposto_percentual = percentual_impostos(salario)
    total_impostos = calular_impostos(salario, imposto_percentual)
    return salario - total_impostos + beneficios

def get_colaborador():
    nome = input("Digite o nome: ")
    salario = float(input("Digite o salário: "))
    beneficios = float(input("Digite o valor dos benefícios: "))
    return { "nome": nome, "salario": salario, "beneficios": beneficios }

def main():
    dados = get_colaborador()
    nome = dados["nome"]
    salario = dados["salario"]
    beneficios = dados["beneficios"]

    novo_salario = novo_salario_final(salario, beneficios)
    print(f"Nome: {nome}")
    print(f"Salário: R$ {novo_salario:.2f}")

main()