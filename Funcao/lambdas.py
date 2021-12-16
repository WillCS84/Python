from functools import reduce

alunos = [
    {'nome': 'Ana', 'nota': 7.2},
<<<<<<< HEAD
    {'nome': 'Breno', 'nota': 9.1},
=======
    {'nome': 'Breno', 'nota': 8.1},
>>>>>>> 2ee06246c9128305ba7b6965ff39dbd7a2a3c09f
    {'nome': 'Claudia', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.7},
]

<<<<<<< HEAD
aluno_aprovado = lambda aluno: aluno['nota'] >= 7
#alunos_honra = filter(lambda aluno: aluno['nota'] >= 9, alunos)
obter_nota = lambda aluno: aluno['nota']
somar = lambda a, b: a + b

alunos_aprovados = list(filter(aluno_aprovado, alunos))
notas_alunos_aprovados = map(obter_nota, alunos_aprovados)
total = reduce(somar, notas_alunos_aprovados, 0)

print(total / len(alunos_aprovados))
=======
alunos_aprovados = list(filter(lambda aluno: aluno['nota'] >= 8, alunos))

print(alunos_aprovados)
>>>>>>> 2ee06246c9128305ba7b6965ff39dbd7a2a3c09f
