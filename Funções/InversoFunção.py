def main ():
    n1 = leNumeroint()
    n2 = leNumeroint()
    res = soma(n1, n2)
    print("A soma é: " ,res   )

def leNumeroint(): 
    numero = input("Digite um numero inteiro: ")
    return int (numero)

def soma(numero1, numero2 ) : 
    resultado = numero1 + numero2
    return resultado

main()