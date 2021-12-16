class Contador:
    contador = 10 # atributo de classe
    
    def inc_maluco (self):
        self.contador = self.contador + 1
        return self.contador

    @classmethod
    def incremento (cls):
        cls.contador += 1
        return cls.contador

    @classmethod
    def decremento (cls):
        cls.contador -= 1
        return cls.contador
    
    @staticmethod
    def mais_um(n):
        return n + 1

c1 = Contador()
print(c1.inc_maluco())
print(c1.inc_maluco())
print(c1.inc_maluco())
print(c1.inc_maluco())

print(Contador.incremento())
# print(Contador.incremento())
# print(Contador.incremento())
# print(Contador.decremento())
# print(Contador.decremento())
# print(Contador.decremento())
# print(Contador.mais_um(99))
