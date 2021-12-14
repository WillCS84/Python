
x = 10

while x:
    print(x)
    x -= 1

print ('Fim!')


total = 0
qtde = 0
nota = 0

while nota != -1:
    nota = float(input('Informe a nota ou -1 para sair: '))
    if nota != -1:
        total += nota
        qtde += 1

print(f'A média da turma é {total/qtde}')

