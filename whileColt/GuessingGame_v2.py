import random

rand_num = random.randint(1,31)

def nums():                                 #? TO MAKE LIST OF STRING INTEGARS
    nums = []
    for i in range(1,31):
        nums.append(str(i))
    return nums

def guess_in(nums):                        #* TO MAKE SURE PLAYER INSERTS A NUMBER BETWEEN 1 and 30
    guess_num = input('Guess a number between 1 to 30: ')

    while guess_num not in nums:
        guess_num = input('Please guess a number between 1 to 30: ')
    else:
        return int(guess_num)

def guessing(guess_num):                   #? TO MAKE THE LOOP RUN UNTIL THE GUESS IS PERFECT
    while rand_num != guess_num:
        diff = abs(rand_num - guess_num)
        if diff >= 10:
            guess_num = input('Too COLD! Try Harder: ')
        elif diff >= 5:
            guess_num = input('WARM! Try few more: ')
        elif diff >= 3:
            guess_num = input('WARMER! Try once more: ')
        elif diff >= 1:
            guess_num = input('Too HOT! I hope you get it this time: ')
        else:
            print('STOP guessing bruh!')
        
        guess_num = int(guess_num)    
    else:
        print('You Won, FINALLY!')

def gameon_choice():                        #* TO KEEP PLAYING OR QUITTING
    choice = 'Wrong'

    while choice not in ['y','n']:
        choice = input('Wanna keep playing? (Y/N): ').lower()

        if choice not in ['y','n']:
            print("Sorry! can't accept, Choose Y or N")
        
    if choice == 'y':
        return True
    else:
        print('Okay! See you again!')
        return False
#?------------------------------------------------------
                    #! GAME PLAY
#?------------------------------------------------------
game_on = True
nums = nums()

while game_on:
    guess_num = guess_in(nums)
    guessing(guess_num)
    game_on = gameon_choice()