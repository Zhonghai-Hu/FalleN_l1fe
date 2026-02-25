# Name: Harrison
# NetID: ki2933
# PROVIDED CODE
# The following code is provided for your use
# Do not make any changes to it or remove
# See the example below to understand how to use
# this example function.
import random
def rpsChoice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)
# End of provided code
## EXAMPLE CODE
## You may use this as an example.
## Comment out or remove
#answer = input("Would you like to see what the computer would choose? yes or no? ")
#if answer.lower() == 'yes':
#    print("The computer chose " + rpsChoice())
#else:
#    print("Ok..")
## End of example code
## Your code goes here

# print the game name
print('Rock Paper Scissors Game')    

# play again
while True:      
    # ask user want to play with computer or Friend                           
    F_or_C = input('Play against a Friend or the computer? Enter F or C: ')
    f_or_c = F_or_C.lower()

    # IF want to play with friend
    if f_or_c == 'f':
        # player enter name
        player_1 = input('Enter name for Player 1: ')
        player_2 = input('Enter name for Player 2: ')

        # store the choice for all player
        player_1_ans = input(f'{player_1} choose Rock, Paper or Scissors: ')
        player_2_ans = input(f'{player_2} choose Rock, Paper or Scissors: ')
        player_1_ans = player_1_ans.lower()
        player_2_ans = player_2_ans.lower()

        print('')

        # tie
        if player_1_ans == player_2_ans:
            print(f'{player_1} chose {player_1_ans}')
            print(f'{player_2} chose {player_2_ans}')
            print('')
            print('Tie Game!')

        # player 1 win
        elif (player_1_ans == 'rock' and player_2_ans == 'scissors') or (player_1_ans == 'scissors' and player_2_ans == 'paper') or (player_1_ans == 'paper' and player_2_ans == 'rock'):
            print(f'{player_1} chose {player_1_ans}')
            print(f'{player_2} chose {player_2_ans}')
            print('')
            print(f'{player_1} Wins!')
        
        # player 2 win
        else:
            print(f'{player_1} chose {player_1_ans}')
            print(f'{player_2} chose {player_2_ans}')
            print('')
            print(f'{player_2} Wins!')
    
    # play with computer
    elif f_or_c == 'c':
        player_2 = input('Enter name for Player 2: ')
        player_2_ans = input(f'{player_2} choose Rock, Paper or Scissors: ')
        player_2_ans = player_2_ans.lower()

        computer_ans = rpsChoice()
        print('')

        # tie
        if computer_ans == player_2_ans:
            print(f'Computer chose {computer_ans}')
            print(f'{player_2} chose {player_2_ans}')
            print('')
            print('Tie Game!')

        # player 1 win
        elif (computer_ans == 'rock' and player_2_ans == 'scissors') or (computer_ans == 'scissors' and player_2_ans == 'paper') or (computer_ans == 'paper' and player_2_ans == 'rock'):
            print(f'Computer chose {computer_ans}')
            print(f'{player_2} chose {player_2_ans}')
            print('')
            print(f'Computer Wins!')
        
        # player 2 win
        else:
            print(f'Computer chose {computer_ans}')
            print(f'{player_2} chose {player_2_ans}')
            print('')
            print(f'{player_2} Wins!')

    else:
        print("Please enter F or C.")
        continue

    # play again
    repeat = input('Do you want play again? (Y or N)  ')
    repeat = repeat.lower()
    if repeat == 'y':
        continue
    else:
        break