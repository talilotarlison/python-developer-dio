def apresentar():
  print("Seja bem vindo!")


def apresentar_pessoa(nome:str, idade:int, cidade):
    print(f"Olá, meu nome é {nome}, tenho {idade} anos e sou de {cidade}.")


def apresentar_nome(nome="anonimo"):
    print(f"Olá, meu nome é {nome}!.")

# Exemplo de uso da função
apresentar()
apresentar_pessoa("João", 30, "São Paulo")
apresentar_nome()
apresentar_nome(nome="joao")

def sucessor_e_antecessor(numero: int):
    sucessor = numero + 1
    antecessor = numero - 1
    return antecessor, sucessor

# Exemplo de uso da função
numero = 5
antecessor, sucessor = sucessor_e_antecessor(numero)
print(f"Antecessor: {antecessor}, Sucessor: {sucessor}")


print(sucessor_e_antecessor(numero))
# https://www.alura.com.br/artigos/conhecendo-as-tuplas-no-python?srsltid=AfmBOoqMhnvoLYSX6H7EBBv_TIpvr0NpIpEVog3iYm4oK15u0agEijgg
print( type(sucessor_e_antecessor(numero)))