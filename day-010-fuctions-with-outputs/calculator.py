from os import system
from calculator_art import logo

def add_number(num1, num2):
    return num1 + num2
def sub_number(num1, num2):
    return num1 - num2
def mult_number(num1, num2):
    return num1 * num2
def div_number(num1, num2):
    return num1 / num2
calc_operation = {
    "+" : add_number,
    "-" : sub_number,
    "*" : mult_number,
    "/" : div_number
}
def calculate_number():
    system('cls')
    print(logo)
    is_continue = True
    num1 = float(input("What's the first number? : "))

    while is_continue:
        for symbol in calc_operation:
            print(symbol)
        calc_symbol = input("Pick an operation. : ")
        num2 = float(input("What's the next number? : "))
        calc_value = calc_operation[calc_symbol](num1, num2)
        print(f"{num1} {calc_symbol} {num2} = {calc_value}")
        end_input = input(f"Type 'y' to continue calculating with {calc_value}, or type 'n' to start new calculation or to exit calculation. : ")
        if end_input == 'y':
            num1 = calc_value
        elif end_input == 'n':
            is_continue == False
            exit_sign = input("Type 'y' to start new calculation or Type 'n' to exit calculation. : ")
            if exit_sign == 'y':
                break
            else:
                print("Good Bye.")
                return

calculate_number()

    
    