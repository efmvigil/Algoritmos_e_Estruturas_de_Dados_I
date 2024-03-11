Produtos = ["Coca-Cola", "Guaraná", "Sprite", "Água"]

Preços = [5.00, 4.50, 4.75, 3.50]

Quantidades = [20, 25, 28, 12]

def imprimirProduto(indice):
    print("Produto: ", Produtos[indice], " Preço: ", Preços[indice], " Quantidade: ",Quantidades[indice])

def removerProduto(indice):
    Produtos.remove(Produtos[indice])
    Quantidades.remove(Quantidades[indice])
    Preços.remove(Preços[indice])
