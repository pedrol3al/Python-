def tem_adjacentes_iguais(numero):
    numero_str = str(numero)
    for i in range(len(numero_str) - 1):
        if numero_str[i] == numero_str[i + 1]:
            return True
    return False

# Entrada do usuário
n = int(input("Digite a quantidade de números: "))
numero = int(input("Digite o número: "))

# Verificação e saída
if tem_adjacentes_iguais(numero): #Teste github
    print("Sim") #Teste github 1
else:
    print("Não")
