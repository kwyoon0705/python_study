from os import system
from art import logo,vs
from game_data import data
import random

def print_logo(scores, end_of_game):
    system('cls')
    print(logo)
    if end_of_game:
        print("Game is OVER.")
    print(f"Your Scores : {scores}")

def play_game(former_word):
    if former_word == {}:
        former_word = random.choice(data)
        data.remove(former_word)
    else:
        former_word = former_word
    print(f"Compare A: {former_word['name']}, a {former_word['description']}, from {former_word['country']}.")
    print(vs)
    latter_word = random.choice(data)
    data.remove(latter_word)
    print(f"Against B: {latter_word['name']}, a {latter_word['description']}, from {latter_word['country']}.")
    submitted_word = input("Who has more followers? Type 'A' or 'B'. : ").lower()
    if submitted_word == 'a':
        if former_word["follower_count"] > latter_word["follower_count"]:
            return former_word
        else:
            return {}
    if submitted_word == 'b':
        if former_word["follower_count"] < latter_word["follower_count"]:
            return latter_word
        else:
            return {}

def init_game():
    end_of_game = False
    scores = 0
    print_logo(scores, end_of_game)
    former_word = {}
    while not end_of_game:
        former_word = play_game(former_word)
        if former_word == {}:
            end_of_game = True
            print_logo(scores, end_of_game)
            break
        scores += 1
        print_logo(scores, end_of_game)
    
init_game()
    