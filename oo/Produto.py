
class produto:
    def __init__(self, nome, preco = 1.99, desc=0):
        self.nome = nome
        self.preco = preco
        self.desc = desc
    
    @property
    def preco_final(self):
        return (1 - self.desc) * self.preco

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco        

p1 = produto('Caneta', 10, 0.1) # produto.__init__(p1)
p2 = produto('Caderno', 14, 0.5)

p1.preco = 70
p2.preco = 1.99

print(p1.nome, p1.preco, p1.desc, p1.preco_final)
print(p2.nome, p2.preco, p1.desc, p2.preco_final)