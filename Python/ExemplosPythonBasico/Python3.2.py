n = int(input("Digite um número inteiro positivo: ")) # entrada de dados

numero = 2
primo = True #primo é a variavel indicadora

while (numero <= n-1) and (primo) : 
    if(n % numero == 0 ): #se n é divisivel por numero
        primo = False
    numero = numero + 1 #soma ao numero para continuar a soma 
if(primo): 
    print("É primo.") #print do resultado
else:
    print("Não é primo.")  #print do resultado