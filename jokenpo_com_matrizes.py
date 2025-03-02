import random
import time

choices = ['Pedra', 'Papel', 'Tesoura']
line = f'{'='*20}\n\n'
repeat = 1

# Matriz de possiveis resultados
jokenpo_results = [['ninguem','eu','você'],
                   ['você','ninguem','eu'],
                   ['eu','você','ninguem']]

# Função principal do jogo
def play():

    # Pergunta a opção do usuario
    player = input("Bem vindo ao Jokenpo do Nubi (versão sem If's)\nEscolha uma opção:\n[0] pedra\n[1] papel\n[2] tesoura\n$ ")
    time.sleep(0.5)

    # Testa se a opção recebida é valida
    try:
        # Tenta transformar a opção do usuario em um indice
        player = abs(int(player))
        player_choice = choices[player]

        # Gera um valor aleatório para o Bot
        bot = random.randint(0,2)
        bot_choice = choices[bot]
    except:
        return print('Opção invalida!')
    
    # Anuncia o ganhador do jogo
    print(f'\nEu joguei {bot_choice} e você jogou {player_choice}.\nO vencedor é... {jokenpo_results[player][bot]}!\n\n')

    # Anuncia o fim de jogo
    time.sleep(0.5)
    print(f'{line}    Fim de jogo!\n\n{line}')
    time.sleep(1)

# Enquanto o valor de repetição não for 0, o jogo repete
while repeat != 0:
    print('\n\n')

    # Inicia o jogo
    play()

    # Pergunta se o usuario quer repetir o jogo
    response = input("\nDeseja jogar novamente?\nDigite 0 para sair.\nOu qualquer tecla para continuar!\n$ ")

    try:
        repeat = int(response)
    except:
        pass
