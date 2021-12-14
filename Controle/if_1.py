nota = float(input('Informe a nota do Aluno: '))
comportado = True if input('Comportado (y/n): ') == 'y' else False

if nota >= 9 and comportado:
    print('Parabéns! :P')
    print('Quadro de Honra')
elif nota >= 7:
    print('Aprovado!!')
else:
    print("Reprovado")

print (nota)
