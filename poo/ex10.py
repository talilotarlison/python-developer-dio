class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento
    
    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
    
    @idade.setter
    def idade(self, nova_idade):
        if nova_idade > 0:
            self._idade = nova_idade
        else:
            raise ValueError("A idade deve ser maior que 0.")
    # Getter e setter nesse formato nao e recomendado em python
    # pois a convencao e usar o decorador property para o getter
    # e o setter para o setter 
    def get_nome(self):
        return self._nome
    
    def set_nome(self, novo_nome):
        self._nome = novo_nome
    
    def get_idade(self):
        return self._idade
    
    def set_idade(self, nova_idade):
        if nova_idade > 0:
            self._idade = nova_idade


pessoa = Pessoa("Guilherme", 1994)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")