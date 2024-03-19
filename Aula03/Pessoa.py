from Cidade import Cidade
class Pessoa:

    def __init__(self, nome, idade=18, cidade = Cidade("Tangamandápio")):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        print("Pessoa ", self.nome, " construída")
