import time
from numpy import random

def vermelho(palavra):
    return '\033[31m'+palavra+'\033[0;0m'

def verde(palavra):
    return '\033[32m'+palavra+'\033[0;0m'

def amarelo(palavra):
    return '\033[33m'+palavra+'\033[0;0m'


def play():
    choices = ['Pedra', 'Papel', 'Tesoura']

    try:
        player1= int(input('\nBem vindo ao Jokenpo do Nubi!\nVocê pode escolher entre:\n1 = Pedra\n2 = Papel\n3 = Tesoura\nQual você escolhe?\n')) - 1
        if player1 > len(choices) or player1 <= 0:
            return print('Você precisa me dizer um numero de 1 á 3 :(')
    except:
        return print('Você precisa me dizer um numero de 1 á 3 :(')

    player2= random.randint(3)
    if player2 == player1:
        print(f'Bot: {choices[player2]}\nVocê: {choices[player1]}\nO jogo {amarelo("empatou")}! ')
    elif (player1 - player2 == -2) or (player1 - player2 == 1):
        print(f'Bot: {choices[player2]}\nVocê: {choices[player1]}\nVocê {verde("ganhou")}!')
    else:
        print(f'Bot: {choices[player2]}\nVocê: {choices[player1]}\nVocê {vermelho("perdeu")}!')

rematch = True
while rematch == True:
    play()
    x = input('Deseja jogar novamente? Digite "s" para sim, e "n" para não!\n')
    if x.lower() in ['s', 'sim']: pass
    else: rematch = False
    time.sleep(0.5)