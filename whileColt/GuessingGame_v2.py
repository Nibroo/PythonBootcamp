import random

rand_num = random.randint(1,31)

def guess_in():                            #* TO MAKE SURE PLAYER INSERTS A NUMBER BETWEEN 1 and 30
    guess_num = input('Guess a number between 1 to 30: ')

    while guess_num not in range(1,31):
        guess_num = int(input('Please guess a number between 1 to 30: '))
    else:
        return int(guess_num)


def guessing(guess_num):                   #? TO MAKE THE LOOP RUN UNTIL THE GUESS IS PERFECT
    while rand_num != guess_num:
        if abs(rand_num - guess_num) >= 10:
            print('Too COLD! Try Harder')
        elif abs(rand_num - guess_num) >= 5:
            print('WARM! Try few more')
        elif abs(rand_num - guess_num) >= 3:
            print('WARMER! Try once more')
        elif abs(rand_num - guess_num) >= 1:
            print('Too HOT! I hope you get it this time')
        else:
            print('STOP guessing bruh!')
        
        guess_num = int(input('Please keep Guessing: '))
    else:
        print('You Won, FINALLY!')

guess_num = guess_in()
guessing(guess_num)