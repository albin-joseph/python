#In this section we are  going to implementr BlackJack Game program
import random
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    random_value = random.randint(0, len(cards)-1)
    return cards[random_value]

random_card = deal_card()
print(f"card value: {random_card}")

user_card = []
computer_card = []

for _ in range(2):
    user_card.extend(deal_card())
    computer_card.extend(deal_card())
    
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

