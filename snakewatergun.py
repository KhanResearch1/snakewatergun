# Welcome Game Play Between Computer ANd User : Snake , Water , Gun:

# First import the random module for random.randint
import random

# define a function 
def mygamePlay(computer, player):
    if computer == player:
        return None
    elif computer == 'snake':
        if player == 'water':
            print('---:(( Snake Finished All your Water :(( ')
            return False
        elif player == 'gun':
            print('--- :)) Great! you Killed Snake With Gun ')
            return True 
    elif computer == 'water':
        if player == 'snake':
            print('--- :)) Great! Your snake finsihed all the water ')
            return True
        elif player == 'gun':
            print('--- :(( So Sad! Your Gun got lost in Water')
            return False 
    elif computer == 'gun':
        if player == 'water':
            print('---  :)) Great! Your Water Ruined Computer\'s Gun')
            return True
        elif player == 'snake':
            print('----- :(( You get killed by Gun')
            return False
    else:
        print('You have entered some wrong message! Try again')

print('Computer Turn:  snake (1) , water (2) , gun (3?')
# for computer turn using random number method
randNO = random.randint(1,3) 

# conditioning for comupter
if randNO == 1:
    computer = 'snake'
elif randNO == 2:
    computer = 'water'
elif randNO == 3:
    computer = 'gun'

player = input('  Your\'s Turn :: { snake  , water , gun }')

a = mygamePlay(computer, player)

print(f"///Computer choose ---> {computer}")

print(f"///You choose ----> {player}")

if a == None:
    print('The game is tie you both choose same turn')
elif a:
    print('Congratulations!!! You Won This Game')
else:
    print(' ohhHh !!! You lost the Game :(......')
         
# ---------------------------------THE END----------------------------------------------------

               





