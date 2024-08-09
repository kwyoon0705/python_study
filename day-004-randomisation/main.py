import random
import rsp_module

player_name = input("Input your player name.\n")

print("################################################")
print("################################################")
print("#### Let's Start Rock, Scissor, Paper Game. ####")
print("################################################")
print("################################################")

# 플레이어가 내는 수
player_value = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))


# 컴퓨터가 내는 수
opponent_value = random.randint(0,2)

value_list = [0, 1, 2, 0, 1, 2]

rsp_art = [rsp_module.rock, rsp_module.paper, rsp_module.scissors]

print(f"{player_name} Choose.")
print(rsp_art[value_list[player_value]])
print("Computer Choose.")
print(rsp_art[value_list[opponent_value]])

if value_list[player_value] == value_list[opponent_value] or value_list[player_value + 3] == value_list[opponent_value] :
    print("Draw.")

if value_list[player_value + 1] == value_list[opponent_value] :
    print("You Lose.")

if value_list[player_value + 2] == value_list[opponent_value] :
    print("You Win.")
    


