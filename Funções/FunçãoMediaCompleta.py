def leNota(num):
    notas = []
    for i in range (num): 
        dados = float(input(f"Digite a nota: "))
        notas.append(dados)
    return notas

def calculaMedia(notas):
    soma = 0 
    for i in range (len(notas)): 
        soma = soma + notas[i]
    return (soma/len(notas))

n = int(input("Digite um número de notas: "))
notas = leNota(n)
print("As notas são:", notas)
media = calculaMedia(notas)
print("A média é: ", format(media, ".1f"))