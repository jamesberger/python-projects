import random
import time

'''
Written by James Berger
February 2022
'''

while True:

    side_chosen = ''

    while side_chosen != True:
        coin_side_choice = input('\n\nWhich side of the coin do you choose? Heads? Or tails? ')

        if coin_side_choice.lower() == 'heads':
            print('You\'ve chosen heads. Your opponent has tails.')
            side_chosen = True
            heads = True
            tails = False
        elif coin_side_choice.lower() == 'tails':
            print('You\'ve chosen tails. Your opponent has heads.')
            side_chosen = True
            heads = False
            tails = True
        else:
            print('What you typed made ZERO sense! You smell funny. Try again!')

    print('Tossing coin...')
    t_end = time.time() + 3
    while time.time() < t_end:
        for i in '|\\-/':
            print('\b' + i, end='')
    print('\n\n')
    coin_sides = ['heads', 'tails']

    random_side = random.choice(coin_sides)

    if random_side == coin_side_choice:
        print(f'Coin lands on {random_side}, you win!')

    if random_side != coin_side_choice:
        print(f'Coin lands on {random_side}, you lose.')

    play_again = input('Do you want to play again? Yes or no? ')

    if play_again.lower() == 'no':
        break
    if play_again.lower() == 'yes':
        print('\n' * 20)
        continue
