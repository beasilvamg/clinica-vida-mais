# Definindo classe pai
class Paciente:
    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

    def __str__(self):
        return f' Nome: {self.nome} | Idade: {self.idade} | Telefone: {self.telefone}\n'