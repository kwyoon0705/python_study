from blackjack_art import logo
import random
from os import system

def deal_card():
    """Returns a random card from the deck."""
    cards = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "king", "queen"]
    card = random.choice(cards)
    return card

def calculate_score(cards_list, is_user):
    if is_user:
        print(f"Your card List : {cards_list}")
    if "ace" in cards_list and not is_user:
        cards_list.remove("ace")
        cards_list.append(11)
    if 11 in cards_list and sum(cards_list) > 21 and not is_user:
        cards_list.remove(11)
        cards_list.append(1)
    if "ace" in cards_list and is_user:
        choose_number = int(input("You have a Ace. You can choice 1 or 11. : "))
        cards_list.remove("ace")
        cards_list.append(choose_number)
    if "king" in cards_list:
        cards_list.remove("king")
        cards_list.append(10)
    if "queen" in cards_list:
        cards_list.remove("queen")
        cards_list.append(10)
    if "jack" in cards_list:
        cards_list.remove("jack")
        cards_list.append(10)
    return sum(cards_list)

def compare_score(my_score, dealer_score):
    print(f"Your Score : {my_score}")
    print(f"Dealer Score : {dealer_score}")
    
    if my_score > 21 and dealer_score > 21:
        return "You went over 21. You Lose."
    if dealer_score > 21:
        return "Dealer went over 21. You Win."
    if my_score > 21:
        return "You went over 21. You Lose."
    if my_score > dealer_score:
        return "You win."
    elif my_score == dealer_score:
        return "Draw."
    elif my_score < dealer_score:
        return "You Lose."
    
def play_game():
    is_over = False
    system('cls')
    my_cards = []
    dealer_cards = []
    my_score = 0
    dealer_score = 0
    print(logo)
    print("Let's start Blackjack.")
    print("==================================================================")
    
    for i in range(0,2):
        my_cards.append(deal_card())
        dealer_cards.append(deal_card())
        
    while not is_over:
        my_score = calculate_score(my_cards, True)
        dealer_score = calculate_score(dealer_cards, False)
        print(f"You got the {my_score} scores.")
        if dealer_score < 17:
                dealer_cards.append(deal_card())
                dealer_score = calculate_score(dealer_cards, False)
                print("Dealer got card.")
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == "y":
            my_cards.append(deal_card())
        if user_should_deal == "n":
            is_over = True
            
    print(f"Your Final Hand : {my_cards} / Dealer's Final Hand : {dealer_cards}")
    print(compare_score(my_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()
