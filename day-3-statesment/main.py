# treasure island

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome To Treasure Island!")
print("Your mission is to find the treasure.")
selection01 = input("You Can Choose A Way. Left or Right?\n")
if selection01 == "Right" or selection01 == "right" :
    selection02 = input("There is a River. Would you Swim or Wait?\n")
    if selection02 == "Wait" or selection02 == "wait" :
        selection03 = input("There are Three Doors. Red, Blue And Yellow. Which one you will choose?\n")
        if selection03 == "red" :
            print("You Burned by fire. GAME OVER.")
        elif selection03 == "blue" :
            print("You Eatened by beasts. GAME OVER.")
        elif selection03 == "yellow" :
            print("You Got the Right Choise. YOU WIN.")
        else :
            print("You choose wrong way. GAME OVER.")
    else :
        print("You Attacked by A plenty of Trouts... GAME OVER.")
else :
    print("You fell into a deep deep dark hole.... You'll die soon... anyway... GAME OVER.")