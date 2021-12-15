from functools import reduce

def atrib(nota):
    return nota + 1.5

notas = [6.4, 7.2, 5.8, 8.4]
notas_finais = map(atrib, notas)

print(notas_finais)