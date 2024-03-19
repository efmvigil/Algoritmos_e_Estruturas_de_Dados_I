from Categoria import Categoria

class Produto:
    def __init__(self, id, nome, preco, qtd, cat = Categoria(nome="Um")):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        self.categoria = cat


