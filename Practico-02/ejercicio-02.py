#Implementar la clase Circulo que contiene un radio, y sus métodos área y perímetro.

import cmath

class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        area = (float("%.2f" % cmath.pi)) * (self.radio**2)
        return area

    def perimetro(self):
        perimetro = 2 * (float("%.2f" % cmath.pi)) * (self.radio)
        return perimetro


circulo = Circulo(4)
assert(circulo.area() == 50.24 and circulo.perimetro() == 25.12)

