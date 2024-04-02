from Cidade import Cidade
from Pessoa import Pessoa
from Produto import Produto
from Categoria import Categoria
from Pedido import Pedido

c1 = Cidade()
c2 = Cidade(nome = "Porto Alegre")
c3 = Cidade(1, "Canoas")

print(c1)
print(c2)
print(c3)

p1 = Pessoa("João")
p2 = Pessoa("Maria", 20)
p3 = Pessoa("José", 25, c1)
p4 = Pessoa("Jorge", cidade = c2)

print(p4.cidade)

cat01 = Categoria("Bebidas")

prod01 = Produto("Coca-Cola", 7.99, cat01)
prod02 = Produto("Pepsi", 5.99, cat01)
prod03 = Produto("Amendoim")

ped01 = Pedido("Rua A, 100", p1)

print(ped01)

total = ped01.addProduto(prod01)
print("Total do Pedido: " + str(total))
total = ped01.addProduto(prod02)
print("Total do Pedido: " + str(total))

