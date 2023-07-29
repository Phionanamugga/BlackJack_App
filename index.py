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
    is_game_over = False

def calculate_score(cards):
   
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    
  # inside calculate_score check for 11, if its there and score is 20, make 11 a 1  
    if 11 in cards and sum(cards) > 21:
        cards.remove(11) 
        cards.append(1)
        return sum(cards)

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f" Your cards: {user_cards}, current score: {user_score}")
    print(f" Computer's first card: {computer_cards[0]}")
    if user_score == 0 or computer_score ==0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True
            
    while computer_score !=0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        
