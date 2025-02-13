dados = {}
contagem = {}
qntletra = 0

chave = input("Digite a chave: ")

pontuacao = [".",",",":",";","!","?"]
for p in pontuacao:
    chave = chave.replace(p,"")

for p in pontuacao:
    chave = chave.replace(" ","")

chave = chave.lower()

for letra in chave:
    qntletra = qntletra + 1
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra] = 1
    
print("A frase contém ",qntletra," letra(s).")
dados[chave] = chave
mais_comum = max(contagem, key=contagem.get)

print(contagem)
print(list("-".join(dados.keys())))
print("\n\n",mais_comum," é a letra mais comum.")