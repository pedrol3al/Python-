texto = input("Digite um texto: ")
pontuação = [".", ",",":","!","?"]

#remove os sinais de pontuação
for p in pontuação :
    texto = texto.replace(p,"")
#Len devolve lista com palavras como itens
numero_palavras = len(texto)
print("Número de palavras: " , numero_palavras)    