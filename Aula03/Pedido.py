from Pessoa import Pessoa

class Pedido:
    def __init__(self, id, end, cli = Pessoa()):
        self.id = id
        self.endereço = end
        self.produtos = []
        self.cliente = cli

    def addProduto(self, nome_produto):
        self.produtos.append(nome_produto)
        Valor = 0
        for produto in (self.produtos):
            Valor = Valor + (produto.preco * produto.qtd)




