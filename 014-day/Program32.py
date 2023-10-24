#Higher or Lower game
import game_data
import random

def play_game():
    a = random.choice(game_data.data)
    b = random.choice(game_data.data)
    if(a['name']==b['name']):
        b = random.choice(game_data.data)
    selection = input(f"Please select which one is higher {a['name']} or {b['name']}? Type 'a' or 'b': ")
    if (selection == 'a'):
        compare(a,b)
    else:
        compare(b,a)
        
def compare(a,b):
    if(a['follower_count'] > b['follower_count']):
        print('You won****')
        play_game()
    else:
        print('You lose @@@@###')
           
play_game()