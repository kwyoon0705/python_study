from auction_art import logo
from os import system # system("cls") : clear console.

def find_bid_winner(bid_data_list):
    highest_bid = 0
    winner_name = ""
    for bid_data in bid_data_list:
        if bid_data["bid"] > highest_bid:
            highest_bid = bid_data["bid"]
            winner_name = bid_data["name"]
    system("cls")
    print(f"Winner is {winner_name}. The Bid is ${highest_bid}.")
    



system("cls")
bid_data_list = []
print(logo)
print("Welcome to the secret auction program.")
is_continue = True
while is_continue:
    bidder_name = input("What is your name? : ")
    bid_price = int(input("What is your bid? : $"))
    bid_data_list.append({"name" : bidder_name, "bid" : bid_price})
    
    continue_bid = input("Are they any other bidders? Type 'yes' or 'no' : ").lower()
    
    if continue_bid == "yes":
        system("cls")
    elif continue_bid == "no":
        is_continue = False   

find_bid_winner(bid_data_list)