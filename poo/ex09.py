# geter e setter em python
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    # Getter para o nome
    @property
    def nome(self):
        return self._nome

    # Setter para o nome
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    # Getter para a idade
    @property
    def idade(self):
        return self._idade

    # Setter para a idade
    @idade.setter
    def idade(self, nova_idade):
        if nova_idade > 0:
            self._idade = nova_idade
        else:
            raise ValueError("A idade deve ser maior que 0.")

# Exemplo de uso
pessoa = Pessoa("João", 25)
print(pessoa.nome)  # João
print(pessoa.idade)  # 25

pessoa.nome = "Maria"
pessoa.idade = 30
print(pessoa.nome)  # Maria
print(pessoa.idade)  # 30