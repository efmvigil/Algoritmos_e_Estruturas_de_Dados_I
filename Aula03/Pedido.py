from Pessoa import Pessoa
from Produto import Produto

class Pedido:
    def __init__(self, end, cli = Pessoa("Anônimo")):
        self.id = None
        self.endereço = end
        self.produtos = []
        self.cliente = cli

    def addProduto(self, produto):
        self.produtos.append(produto)
        Valor = 0
        for produto in (self.produtos):
            Valor += produto.preco

        return Valor

    def _str_(self):
        texto = "Endereço do Pedido: " + self.end
        texto += "\n Cliente: " + self.cliente.nome
        texto += "\nProdutos: \n"
        for p in self.produtos:
                texto += p.nome + " - " + str(produto.preco) + " - Cat: " + produto.cat.nome + "\n"
        return texto





