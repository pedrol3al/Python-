class TV():
    def __init__(self, cor, tamanho):  
        self.cor = cor
        self.ligada = False
        self.tamanho = tamanho
        self.canal = "Netflix"
        self.volume = 50

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal

    def mudar_volume(self):
        pass

    def ligar_desligar(self):
        pass

#programa
tv_sala = TV(cor = 'Preta', tamanho=55)
tv_quarto = TV('Branca', tamanho=29)
tv_sala.mudar_canal('Globo')
tv_quarto.mudar_canal('Youtube')

print(tv_quarto.cor)
print(tv_quarto.tamanho)
print(tv_quarto.canal)
print(tv_quarto.volume,"\n")

print(tv_sala.cor)
print(tv_sala.tamanho)
print(tv_sala.canal)
print(tv_sala.volume)

