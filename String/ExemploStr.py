a = "Fizeram as atividades?\n"
print(a)

b = "20 de abril tem prova. "
print(b[0]) #O colchete serve pra selecionar a posição do que vai aparecer para o usuario

c = "Fizeram\nOs\nExercicios?" #Pula linha "\n"
print(c) 

print(b + c) #Soma das strings

print(5 * a ) #Multiplica a variavel selecionada pela quantidade de vezes desejada

string = input("Digite um texto: ")
inversa = " "
for x in string: #Inverte um texto inserido pelo usuario
    inversa = x + inversa
print(inversa)

print(b[6:11]) #Corta entre a quantidade de caracteres na string
print(b[6:11:2]) #Corta de dois em dois por conta do "":2"
print(b[: : -1 ]) #Inverte uma string 

print(a)
print(a.strip(), "oi") #Retira os cortes de linha

resultado = "exercicios" in "fizeram os exercicios? "
print(resultado) #Procura palavras-chave dentro de frases