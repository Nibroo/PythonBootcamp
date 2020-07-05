def display_game(game_list):
    print ("Here's the Game list:")
    print(game_list)


def position_choice():
    
    choice = 'Wrong'

    while choice not in ['0','1','2']:
        print('Please choose a Number (0,1,2): ')

        if choice not in ['0','1','2']:
            print('Sorry! Invalid Choice')
        
    return int(choice)


def replacement_choice(game_list,position):
    user_placement = input('Type a string or value to replace at position: ')

    game_list[position] = user_placement

    return game_list


def gameon_choice():
    
    choice = 'Wrong'

    while choice not in ['Y','N']:
        print('Wanna keep playing? (Y/N): ')

        if choice not in ['Y','N']:
            print("Sorry! can't accept, Choose Y or N")
        
    if choice == 'Y':
        return True
    else:
        print('Okay! See you again!')
        return False


game_on = True
game_list = [0,1,2]

while game_on:
    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list,position)

    display_game(game_list)

    game_on = gameon_choice()