import random
import time

game_data = [' '] * 9   # initialize game data to an empty array

symbol_determined = False
player_symbol = input('Would you like to be x or o?')
while not symbol_determined:
    if player_symbol.lower() == 'x':
        computer_symbol = 'o'
        symbol_determined = True
    elif player_symbol.lower() == 'o':
        computer_symbol = 'x'
        symbol_determined = True
    else:
        print('Please choose \'x\' or \'o\' to continue.')
        player_symbol = input('Would you like to be x or o?')

first_determined = False
while not first_determined:
    preference = input('Would you like to go first? (enter \'yes\' or \'no\')')
    if preference.lower() == 'yes':
        whose_turn = 'player'
        first_determined = True
    elif preference.lower() == 'no':
        whose_turn = 'computer'
        first_determined = True
    else:
        print('Please enter \'yes\' or \'no\' to continue.')
        
occupied = []

def print_board(game_data):
    print()
    print('', game_data[6], '|', game_data[7], '|', game_data[8], '       7 | 8 | 9 ')
    print('-'* 11, '    ', '-'* 11)
    print('', game_data[3], '|', game_data[4], '|', game_data[5], '       4 | 5 | 6 ')
    print('-'* 11, '    ', '-'* 11)
    print('', game_data[0], '|', game_data[1], '|', game_data[2], '       1 | 2 | 3 ')
    print()

terminate = False
def endgame(first_slot, second_slot, third_slot, slots:list, line:str):
    global terminate
    global occupied
    if first_slot == second_slot and first_slot == third_slot and first_slot in occupied:
        if first_slot == player_symbol:
            print('You won this game! Thank you for playing.')
            terminate = True
        if first_slot == computer_symbol:
            print('The computer won this game. Thank you for playing!')
            terminate = True
        game_data[slots[0]] = line
        game_data[slots[1]] = line
        game_data[slots[2]] = line
        print_board(game_data)
    if len(occupied) == 9 and not terminate:
        print('This game has ended in a tie. Thank you for playing!')
        terminate = True
    else:
        pass

block = False
move = ' '
def strategy(slots:list):
    global block
    global move
    first_slot = game_data[slots[0]]
    second_slot = game_data[slots[1]]
    third_slot = game_data[slots[2]]
    if (first_slot == second_slot and third_slot not in occupied and first_slot in occupied and second_slot in occupied):
        block = True
        move = slots[2]
    elif (first_slot == third_slot and second_slot not in occupied and first_slot in occupied and third_slot in occupied):
        block = True
        move = slots[1]
    elif (second_slot == third_slot and first_slot not in occupied and third_slot in occupied and second_slot in occupied):
        block = True
        move = slots[0]
    else:
        pass
    
def end_check():
    endgame(game_data[0], game_data[1], game_data[2], [0, 1, 2], '-')
    endgame(game_data[3], game_data[4], game_data[5], [3, 4, 5], '-')
    endgame(game_data[6], game_data[7], game_data[8], [6, 7, 8], '-')
    endgame(game_data[0], game_data[3], game_data[6], [0, 3, 6], '|')
    endgame(game_data[1], game_data[4], game_data[7], [1, 4, 7], '|')
    endgame(game_data[2], game_data[5], game_data[8], [2, 5, 8], '|')
    endgame(game_data[6], game_data[4], game_data[2], [6, 4, 2], '\\')
    endgame(game_data[0], game_data[4], game_data[8], [0, 4, 8], '/')

def strat_check():
    strategy([0, 1, 2])
    strategy([3, 4, 5])
    strategy([6, 7, 8])
    strategy([0, 3, 6])
    strategy([1, 4, 7])
    strategy([2, 5, 8])
    strategy([6, 4, 2])
    strategy([0, 4, 8])
        
while True:
    print_board(game_data)
    
    end_check()
    strat_check()
    if terminate:
        break
    
    if whose_turn == 'player':
        selection = input('Where would you like to go? (1-9 to play, Q to quit)')
        if selection.upper() == 'Q':
            print ('Quitting game...')
            break
        try:
            selection = int(selection) - 1
            if selection < 0:
                print('You must choose a spot on the board using the numbers 1-9 in integer format')
                continue
            elif game_data[selection] in occupied:
                print('You cannot go in a slot that has already been occupied. Please choose another slot.')
                continue
            else:
                game_data[selection] = player_symbol
                print_board(game_data)
                whose_turn = 'computer'
                occupied.append(game_data[selection])
        except:
            print('You must choose a spot on the board using the numbers 1-9 in integer format')
            continue

    end_check()
    strat_check()
    if terminate:
        break

    if whose_turn == 'computer':
        print('handle computer\'s turn')
        time.sleep(0.1)
        if block:
            selection = move
            spot_determined = False
            while not spot_determined:
                if game_data[selection] in occupied:
                    selection = random.randint(0,8)
                else:
                    spot_determined = True
            game_data[selection] = computer_symbol
            occupied.append(game_data[selection])
            whose_turn = 'player'
        else:
            selection = random.randint(0,8)
            spot_determined = False
            while not spot_determined:
                if game_data[selection] in occupied:
                    selection = random.randint(0,8)
                else:
                    spot_determined = True
            game_data[selection] = computer_symbol
            occupied.append(game_data[selection])
            whose_turn = 'player'
        


    # TODO (for HW5): each time either the computer plays, 
    # check if someone won or if there's a tie.

##        outcome_determined = False
##        while not outcome_determined:
##            new_game = input('This game has ended in a tie. Would you like to play again? (enter \'yes\' or \'no\')')
##            try:
##                if new_game.lower() == 'yes':
##                    first_determined = False
##                    outcome_determined = True
##                    game_data = [' ']*9
##                elif new_game.lower() == 'no':
##                    print('Quitting...')
##                    break
##            except:
##                print('Please enter \'yes\' or \'no\' to continue or quit.')
    

