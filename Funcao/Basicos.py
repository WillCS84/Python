#!Python3

def saudacao(nome = 'Pessoa', idade = 20):
    print(f'Bom Dia {nome}!\nVc nem parece ter {idade} anos')

#def saudacao():
#    print('Boa Tarde')

def soma_e_multi(a, b, x):
    return a + b * x

if __name__ == '__main__':
    saudacao('Ana',idade=30)