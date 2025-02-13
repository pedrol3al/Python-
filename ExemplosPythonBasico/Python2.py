class Pessoa: 
    nome = "tati"
    idade = 0
    peso = 0
    altura = 0

    def envelhecer(self, valor ):
      self.idade += valor

    def engordar(self,valor):
        self.peso += valor

    def emagrecer(self,valor):
     self.peso -= valor

    def crescer(self,valor): 
      self.altura += valor

if __name__ == '__main__': 
        pessoa =  Pessoa()
        pessoa.idade = 16
        pessoa.peso = 54
        pessoa.altura = 1.55 
        pessoa.crescer(0.05)
        pessoa.engordar(2)
        pessoa.envelhecer(1)
        pessoa.emagrecer(1)
        print(pessoa.nome)
        print(pessoa.idade)
        print(pessoa.peso)
        print(pessoa.altura)