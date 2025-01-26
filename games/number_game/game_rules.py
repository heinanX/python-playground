def read_rules():
        init_rules = input('Do you need the rules? (y/n) ').lower()
        if init_rules == 'yes' or init_rules == 'y':
            print('Choose a number between 10 and 999, then try to guess the correct one! The fewer tries you take, the higher your score. Need help? Hints are available!')
            return
        else:
            return