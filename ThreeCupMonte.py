from random import shuffle

def shuffle_list(alist):                                        #? FOR SHUFFLING THE LIST
    shuffle(alist)
    return alist

def player_guess():                                             #? FOR GETTING INPUT FROM THE PLAYER
    
    guess = ''
    while guess not in ['0','1','2']:
        guess = input('Guess any spot from 0, 1 or 2 : ')
    
    return int(guess)

def check(olist, guess):                                      #? FOR CHECKING THE GUESS and THE LIST
    if olist[guess] == 'O':
        print('PERFECT GUESS!')
    else:
        print('WRONG! TRY AGAIN BUDDY')
        print ('The list was: ' + str(mixed_up_list))


my_list = [' ', 'O', ' ']                           #! Primary List

mixed_up_list = shuffle_list(my_list)               #! Shuffled List

guess = player_guess()                              #! PLayer Input

check(my_list, guess)                               #! Checking & Final Output

