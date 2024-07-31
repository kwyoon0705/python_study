import ascii_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
            'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

is_end = False
wrong_direction = False
wrong_text = False
wrong_shift_number = False
print(ascii_art.logo)
def crypt_function(direction, text, shift_number):
    crypted_text = ""
    for letter in text:
        index = alphabet.index(letter) + shift_number
        if direction == "decode":
            index = alphabet.index(letter, 26) - shift_number
        crypted_text += alphabet[index]
    print(f"The {direction}d text is ::: {crypted_text}.")
        
while not is_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt. : \n").lower()
    if direction != "encode" and direction != "decode":
        wrong_direction = True
    while wrong_direction:
        direction = input("You typed wrong word. Please type 'encode' to encrypt or type 'decode' to decrypt. : \n").lower()
        if direction == "encode" or direction == "decode":
            wrong_direction = False
    text = input("Type your message. : \n").lower()
    for char in text:
        if char not in alphabet:
            wrong_text = True
            break
    while wrong_text:
        text = input("You typed wrong message. Type your message correctly. : \n").lower()
        count = 0
        for char in text:
            if char in alphabet:
                count += 1
        if count == len(text):
            wrong_text = False
    shift_number = int(input("Type the shift number : \n")) % 26
    crypt_function(direction, text, shift_number)
    is_continue = input("Do you want to continue? Y or N : \n").lower()
    if is_continue == "y":
        continue
    elif is_continue =="n":
        is_end = True
        print("Goodbye.")
