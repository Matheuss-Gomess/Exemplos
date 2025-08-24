class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self. altura = altura

    def calcular_area(self):
        area = (self.base * self.altura) / 2
        return area
    
triangulo1 = Triangulo(base=10, altura=5)
area_triangulo1 = triangulo1.calcular_area()

print("Area do triangulo: ", area_triangulo1)