# Solicita ao usuário a quantidade de números que serão analisados
n = int(input("Digite uma quantidade de números para ser analisada: "))  

# Solicita o primeiro número e armazena na variável 'anterior'
print("Informe o número: ")
anterior = int(input())

# Variável indicadora que assume True caso os números estejam ordenados
ordenado = True  

for i in range(n-1): 

    print("Informe o número: ")
    atual = int(input())  # Lê o próximo número

    if (atual < anterior):  
        ordenado = False  # Se for menor, a sequência não está ordenada
        break # Quebra de codigo
    anterior = atual  # Atualiza o valor de 'anterior' para a próxima comparação

# Após o loop, verifica se a sequência permaneceu ordenada
if ordenado:  
    print("Sequência ordenada.")
else:
    print("Sequência não ordenada.")
