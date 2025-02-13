string = input("Digite um texto: ") #Entrada de dados
inversa = ""

string = string.lower()

pontuação = [".", ",",":","!","?"]

#remove os sinais de pontuação
for p in pontuação :
    string = string.replace(p,"")

for x in string: #Verificação se a palavra é palíndromo
    inversa = x + inversa
print(inversa)
 
if string == inversa: 
    print("É um palíndromo")
else: 
    print("Não é um palíndromo")