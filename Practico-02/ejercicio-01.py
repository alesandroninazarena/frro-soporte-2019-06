#Implementar la clase Rectangulo que contiene una base y una altura, y el método area.


class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        area = self.base * self.altura
        return area


rectangulo = Rectangulo(2, 5)
assert(rectangulo.area() == 10)






