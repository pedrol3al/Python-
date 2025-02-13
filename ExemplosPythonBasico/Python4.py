# Solicita ao usuário a quantidade de números que serão analisados
n = int(input("Digite uma quantidade de números para ser analisada: "))  

# Solicita o primeiro número e armazena na variável 'anterior'
print("Informe o número: ")
anterior = int(input())

# Inicializa o contador 'i' para rastrear a quantidade de números lidos
i = 1  # Já lemos um número

# Variável indicadora que assume True caso os números estejam ordenados
ordenado = True  

# Loop que percorre os próximos números informados pelo usuário
while (i < n) and (ordenado):  # Enquanto ainda houver números para ler e a sequência estiver ordenada
    print("Informe o número: ")
    atual = int(input())  # Lê o próximo número
    i = i + 1  # Incrementa o contador de números lidos
    
    # Verifica se o número atual é menor que o anterior
    if (atual < anterior):  
        ordenado = False  # Se for menor, a sequência não está ordenada
    anterior = atual  # Atualiza o valor de 'anterior' para a próxima comparação

# Após o loop, verifica se a sequência permaneceu ordenada
if ordenado:  
    print("Sequência ordenada.")
else:
    print("Sequência não ordenada.")
