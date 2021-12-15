from functools import reduce

def somar_nota(delta):
    def somar(nota):
        return nota + delta
    return somar

notas = [6.4, 7.2, 5.4, 8.4]
notas_finais_1 = map(somar_nota(1.5), notas)
notas_finais_2 = map(somar_nota(1.6), notas)

print(notas_finais_1)
print(notas_finais_2)

def somar(a, b):
    return a + b

total = reduce (somar, notas, 0)
print(total)