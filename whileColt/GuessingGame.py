import random

rand_num = random.randint(1, 31)


def guess_in():  # * TO MAKE SURE PLAYER INSERTS A NUMBER BETWEEN 1 and 30
    guess_num = int(input('Please guess a number between 1 to 30: '))

    while guess_num not in range(1, 31):
        guess_num = int(input('Please guess a number between 1 to 30: '))

    else:
        return int(guess_num)


def guessing(guess_num):  # ? TO MAKE THE LOOP RUN UNTIL THE GUESS IS PERFECT
    while rand_num != guess_num:
        if rand_num > guess_num:
            print('Too Low! Try Again')
        elif rand_num < guess_num:
            print('Too High! Try Again')
        else:
            print('Not even close bruh!')

        guess_num = int(input('Please guess a number between 1 to 30: '))
    else:
        print('You Won, FINALLY!')


guess_num = guess_in()
guessing(guess_num)
