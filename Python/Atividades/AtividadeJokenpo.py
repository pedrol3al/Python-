from random import randint  # Importa a função randint para gerar números aleatórios

def jogar():  # Define uma função para permitir jogar novamente
    itens = ('Pedra', 'Papel', 'Tesoura')  # Cria uma tupla com as opções do jogo
    computador = randint(0, 2)  # O computador escolhe um número aleatório entre 0 e 2
    
    print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')  # Mostra as opções disponíveis
    
    while True:
        try:  #Permite que o codigo continue sendo executado mesmo havendo erros 
            jogador = int(input("Qual é a sua jogada? "))  # Pede a escolha do jogador
            if jogador in (0, 1, 2):  # Verifica se a escolha é válida
                break  # Sai do loop caso a entrada seja válida
            else:
                print("Erro! Escolha inválida. Digite 0, 1 ou 2.")  # Mensagem de erro para entrada inválida
        except ValueError:  # Printa o erro do usuario
            print("Erro! Entrada inválida. Digite um número entre 0 e 2.")
    
    print('-=' * 11)  # Adiciona uma linha para separação do resultado
    print(f'Computador jogou {itens[computador]}')  # Exibe a escolha do computador
    print(f'Jogador jogou {itens[jogador]}')  # Exibe a escolha do jogador
    print('-=' * 11)
    
    # Determina o resultado do jogo
    if computador == jogador:
        print("Empate!")
    elif (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):
        print("Você venceu!")
    else:
        print("Você perdeu!")
    
    # Pergunta se o usuário quer jogar novamente
    novamente = input("Deseja jogar novamente? (s/n): ").strip().lower()
    if novamente == 's':
        jogar()  # Chama a função novamente para reiniciar o jogo

# Chama a função pela primeira vez para iniciar o jogo
jogar()
