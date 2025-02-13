n = int(input("Insira uma quantidade de números para ser analisada: "))
print("Informe o número: ")
anteriror = int(input())

i = 1 #leu 1 numero
ordenado = 0 #ordenado é a variavel controladora

while(i < n) and (ordenado == 0 ):
    print("informe o número : ")
    atual = int(input())
    i = i + 1
    if(atual <= anteriror ): 
        ordenado = ordenado + 1
    anteriror = atual

if (ordenado == 0 ): 
    print("Sequência está ordenada. ")
else:
    print("Sequência não está ordenada. ")    