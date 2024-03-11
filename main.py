def getPi():
    return 3.14

def calcularAreaCirculo(raio):
    area = getPi() * (raio * raio)
    return area

def imprimirAreaCirculo(raio):
    area = getPi() * (raio * raio)
    print("Área do circulo: ", area)

imprimirAreaCirculo(3)
