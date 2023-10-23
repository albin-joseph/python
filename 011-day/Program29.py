#In this section we are  going to implementr BlackJack Game program
import random
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    random_value = random.randint(0, len(cards)-1)
    return cards[random_value]

random_card = deal_card()
print(f"card value: {random_card}")
  
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "Yo Win"
    else:
        return "You lose"
    

def play_game():
    user_card = []
    computer_card = []
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())


    while not is_game_over:   
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True 
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass:")
            if user_should_deal == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True
            
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
        
    print(f"user score {user_score}")
    print(f"compauter score {computer_score}")   
    print(compare(user_score, computer_score)) 

while input("Do you wnat to play the game Blackjack? type 'y' or 'n': ") == "y":
    play_game()