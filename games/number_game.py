import random

# Smaller functions
def read_rules():
        init_rules = input('Do you need the rules? (y/n) ').lower()
        if init_rules == 'yes' or init_rules == 'y':
            print('Choose a number between 10 and 999, then try to guess the correct one! The fewer tries you take, the higher your score. Need help? Hints are available!')
            return
        else:
            return

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

def set_max_num():
     while True:
        try:
            max_num = int(input('First, enter a number (between 10-999): '))
            if max_num < 999 and max_num > 10:
                win_num = random.randint(1, max_num)
                return win_num
            else:
                print('please enter a number between 10 - 999')
        except ValueError:
            print('That\'s not a valid number, buddy. Try again :3')

# Game
print('Welcome to Guess the Number!')
read_rules()

if game_start():
    win_num = set_max_num()
    print(win_num)
    print('Great work! Now it\'s time to start guessing!')
    attempts = 0

    while True:
        guess = int(input('Enter your guess: '))
        attempts += 1
        if guess == win_num:
            print('Congratulations you won! You managed to score: ' + str(attempts) )
            break
        else:
            if win_num > guess:
                print('A little higher than that')
            else:
                print('A little bit lower than that')
else:
    print('D\'aww that\'s too bad...')

