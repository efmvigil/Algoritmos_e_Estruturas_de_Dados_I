from Cidade import Cidade
from Pessoa import Pessoa

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
