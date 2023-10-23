#Number guess program
import random

EASY_LEVEL = 10
HARD_LEVEL = 5

actual_value = random.randint(1,100)

def check_guess(guess_value):
    print(f"actual_value: {actual_value}")
    if(guess_value == actual_value):
        print("You won")
        return True
    elif(guess_value > actual_value):
        print("Too high")
        return False
    else:
        print("Too low")
        return False
    
def play_game():
    difficulties = {"easy": EASY_LEVEL, "hard": HARD_LEVEL}
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    difficulty_value = difficulties[difficulty]
    for i in range(0,difficulty_value):
        print(f"You have remaining {difficulty_value - i}")
        guess_number = int(input('Guess a number between (1,100): '))
        if(check_guess(guess_number)):
            break
        
play_game()
        
        
        
        
    