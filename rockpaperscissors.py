import random

move_set = ['rock', 'paper', 'scissors']

score = []


def game_logic(player, player_2):   # Rock Paper Scissors Logic

    if player == 'rock' and player_2 == 'scissors':
        print('%s beats %s' % (player, player_2))
        print('Player1 wins!')
        score.append(1)

    elif player == 'paper' and player_2 == 'rock':
        print('%s beats %s' % (player, player_2))
        print('Player1 wins!')
        score.append(1)

    elif player == 'scissors' and player_2 == 'paper':
        print('%s beats %s' % (player, player_2))
        print('Player1 wins!')
        score.append(1)

    elif player == player_2:
        print('draw')

    else:
        print('%s beats %s' % (player_2, player))
        print('Player2 wins!')
        score.append(2)


def who_won():

    if score.count(1) > 2:
        print('Player 1 is victorious')

    elif score.count(2) > 2:
        print('Player 2 is victorious')


def player_vs_cpu():

    while len(score) < 6:

        if score.count(1) > 2 or score.count(2) > 2:
            break

        player_choice = input('rock, paper or scissors: ')
        cpu_choice = random.choice(move_set)

        game_logic(player_choice, cpu_choice)


def cpu_vs_cpu():

    while len(score) < 6:

        if score.count(1) > 2 or score.count(2) > 2:
            break

        cpu_choice = random.choice(move_set)
        cpu_choice_2 = random.choice(move_set)

        game_logic(cpu_choice, cpu_choice_2)


def player_vs_player():

    while len(score) < 6:

        if score.count(1) > 2 or score.count(2) > 2:
            break

        player_choice = input('rock, paper or scissors: ')

        for i in range(0, 41):   # Hides player_choice from player_choice_2
            print('-')

        player_choice_2 = input('rock, paper or scissors: ')

        game_logic(player_choice, player_choice_2)


def main():

    print('Welcome to RockPaperScissors \n Chose your game mode')
    selector = input('pvp, pvc, cvc: ')

    if selector == 'pvp':
        player_vs_player()
        who_won()

    elif selector == 'pvc':
        player_vs_cpu()
        who_won()

    elif selector == 'cvc':
        cpu_vs_cpu()
        who_won()


if __name__ == '__main__':
    main()
