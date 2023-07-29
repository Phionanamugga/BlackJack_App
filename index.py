# Import a random module 
# create a deal_card function that picks and returns a random card from the list of cards

import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    
  # inside calculate_score check for 11, if its there and score is 20, make 11 a 1  
    if 11 in cards and sum(cards) > 21:
        cards.remove(11) 
        cards.append(1)
        return sum(cards)

# checking for a Blackjack
#     
