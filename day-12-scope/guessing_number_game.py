from os import system
import random
from guessing_number_game_art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def game_init():
    system('cls')
    print(logo)
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of number between 1 and 100.")
    is_end = False
    answer_number = random.randint(1, 100)
    attempt_chance = set_difficulty()
    
    print(f"You have {attempt_chance} attempts remaining to guess the number.")
    
    while not is_end:
        attempt_chance = guess_number(answer_number, attempt_chance)
        if attempt_chance == 100:
            is_end = True
            break
        elif attempt_chance != 100 and attempt_chance != 0:
            print(f"You have {attempt_chance} attempts remaining to guess the number.")
        elif attempt_chance == 0:
            print("You have no attempts remaining to guess the number.")
            print("You Lose.")
            is_end = True
            break

def guess_number(answer_number, attempt_chance):
    guessing_number = int(input("Make a guess : "))
    if guessing_number == answer_number:
        print(f"You Got it. The answer is {answer_number}")
        return 100
    elif guessing_number > answer_number:
        print("Too high.")
    elif guessing_number < answer_number:
        print("Too low.")
    return attempt_chance - 1
    
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'. : ")
    if difficulty == 'easy':
        return EASY_LEVEL_TURNS
    elif difficulty == 'hard':
        return HARD_LEVEL_TURNS

game_init()