import random
from scoresheet import scoresheet
from game_rules import read_rules

# Variables
invalid_number_warning = print('That\'s not a valid number, buddy. Try again :3')

# Smaller functions
def game_start():
    while True:
        init_game = input('So, do you want to play? (y/n) ').lower()
        if init_game == 'yes' or init_game == 'y':
            print('Wooo! Let\'s go!')
            return True
        elif init_game == 'no' or init_game == 'n':
            return False
        else:
            print('must be a yes or no answer')

def set_game_mode(num):
    print('this is ' + str(num))
    if scoresheet["easy"]["range"][0] <= num <= scoresheet["easy"]["range"][1]:
        return 'easy'
    elif scoresheet["standard"]["range"][0] <= num <= scoresheet["standard"]["range"][1]:
        return 'standard'
    elif scoresheet["hard"]["range"][0] <= num <= scoresheet["hard"]["range"][1]:
        return 'hard'
    elif scoresheet["extra_hard"]["range"][0] <= num <= scoresheet["extra_hard"]["range"][1]:
        return 'extra_hard'
    else:
        return 'insane'

def set_max_num():
     while True:
        try:
            max_num = int(input('First, enter a number (between 10-999): '))
            if max_num < 999 and max_num > 10:
                game_mode = set_game_mode(max_num)
                win_num = random.randint(1, max_num)
                return win_num, game_mode
            else:
                print('please enter a number between 10 - 999')
        except ValueError:
            invalid_number_warning


# Game
print('Welcome to Guess the Number!')
read_rules()

if game_start():
    win_num, game_mode = set_max_num()
    print('this is game mode ' + game_mode)
    print(win_num)
    print('Great work! Now it\'s time to start guessing!')
    attempts = 0

    while True:
        try:
            guess = int(input('Enter your guess: '))
        except ValueError:
            invalid_number_warning
        attempts += 1
        if guess == win_num:
            print('Congratulations you won! You managed to score: ' + str(attempts))
            game_start()
            break
        else:
            if win_num > guess:
                print('A little higher than that')
            else:
                print('A little bit lower than that')
else:
    print('D\'aww that\'s too bad...')

