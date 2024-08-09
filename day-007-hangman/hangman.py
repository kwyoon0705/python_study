import random
import hangman_ascii
import hangman_word

word_list = hangman_word.word_list
ascii_picture = hangman_ascii.stages
chosen_word = random.choice(word_list)
chosen_letter_list = []
for number in range(0,len(chosen_word)):
    chosen_letter_list += "_"
is_correct = False
player_life = 6
print(hangman_ascii.logo)
print(f"remained life : {player_life}")
while not is_correct:
    guessing_letter = input(f"Guess A word : ").lower()
    index = 0
    match_count = 0
    for letter in chosen_word:
        if letter == guessing_letter:
            chosen_letter_list[index] = guessing_letter
            match_count += 1
        index += 1
    if match_count == 0:
        player_life -= 1
        print("No Matches. You lose a life.")
    print(f"{ascii_picture[player_life]}")
    print(chosen_letter_list)
    print(f"remained life : {player_life}")
    if player_life == 0 :
        print("GAME OVER.")
        break
    elif player_life > 0:
        if "_" not in chosen_letter_list:
            print("You Win.")
        
        
        
            
