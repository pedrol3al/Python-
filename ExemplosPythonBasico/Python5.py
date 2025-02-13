# Solicita ao usuário um número inteiro positivo
n = int(input("Digite um número inteiro positivo: "))

numero = 2
divisores = 0  # Variável contadora de divisores

# Loop para verificar quantos divisores diferentes de 1 e n existem
while numero <= n - 1:
    if n % numero == 0:  # Se for divisível, incrementa o contador
        divisores += 1
    numero += 1

# Ajuste para garantir a lógica correta
if divisores == 0:  # Se não houver divisores além de 1 e n, o número é primo
    print(n, "é primo.")
elif divisores == 1:  # Caso especial para números que possuem apenas 1 divisor além de 1 e n
    print(n, "não é primo. Possui 1 divisor diferente de 1 e", n)
else:  # Se houver mais de 1 divisor além de 1 e n, não é primo
    print(n, "não é primo. Possui", divisores, "divisores diferentes de 1 e", n)
