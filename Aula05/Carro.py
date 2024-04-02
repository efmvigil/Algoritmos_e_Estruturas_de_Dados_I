from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, ano, cat, qtdPortas):
        super().__init__(marca, ano, cat)
        self.qtdPortas = qtdPortas


    def __str__(self):
        texto = super().__str__()
        texto += "Portas: " + str(self.qtdPortas)
        return  texto

    def imprimir(self):
        super().imprimir()

