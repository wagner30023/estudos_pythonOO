
class Calculadora:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        resultado = self.a + self.b
        print(resultado)

    def subtracao(self):
        resultado = self.a - self.b
        print(resultado)

    def divisao(self):
        resultado = self.a / self.b
        print(resultado)

    def multiplicao(self):
        resultado = self.a * self.b
        print(resultado)

    def potencia(self):
        resultado = self.a ** self.b
        print(resultado)

    def impressao(self, a):
        print(a)



