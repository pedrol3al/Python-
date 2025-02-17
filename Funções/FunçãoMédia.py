# Cria uma lista vazia para armazenar as notas
notas = []

# Solicita ao usuário que digite a quantidade de notas que ele deseja informar
n = int(input("Digite a quantidade de notas: "))

# Laço para solicitar ao usuário que digite cada nota
for i in range(n): 
    # Pede ao usuário para digitar a nota correspondente à posição (i + 1)
    dados = float(input(f"Digite a nota {i + 1}: "))
    
    # Adiciona a nota informada à lista de notas
    notas.append(dados)
    
    # Exibe a lista de notas atualizada
    print(notas)

# Inicializa uma variável para acumular a soma das notas
soma = 0 

# Laço para iterar sobre a lista de notas e calcular a soma total
for i in range(len(notas)): 
    # Adiciona o valor da nota atual à soma
    soma = soma + notas[i]

# Calcula a média das notas dividindo a soma pelo número total de notas
media = soma / len(notas)

# Exibe a média das notas, formatada com uma casa decimal
print(format(media, ".1f"))
