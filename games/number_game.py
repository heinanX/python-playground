max_num = 0
attempts = 0

def game_start():
    while True:
        init_game = input('So, do you want to play? (yes/no)').lower()
        if init_game == 'yes' or init_game == 'y':
            print('Wooo! Let\'s go!')
            return True
        elif init_game == 'no' or init_game == 'n':
            return False
        else:
            print('must be a yes or no answer')
    
def read_rules():
        init_rules = input('Do you need the rules? (yes/no)').lower()
        if init_rules == 'yes' or init_rules == 'y':
            print('Choose a number between 10 and 999, then try to guess the correct one! The fewer tries you take, the higher your score. Need help? Hints are available!')
            return
        else:
            return


print('Welcome to Guess the Number')
read_rules()
if game_start():
    max_num = int(input('First, enter a number (between 10-999):'))
    print('Great work! Now it\'s time to start guessing!')
    while True:
        guess = int(input('enter your guess'))
        attempts += 1
        if guess == max_num:
            print('Congratulations you won! You managed to score:')
            break
        else:
            if max_num > guess:
                print('a little higher than that')
            else:
                print('a little bit lower than that')
else:
    print('D\'aww that\'s too bad...')

