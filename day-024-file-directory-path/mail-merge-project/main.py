with open("Input/Names/invited_names.txt", "r") as names:
    name_list = names.readlines()

with open("Input/Letters/starting_letter.txt", mode="r") as ref_letter:
    letter_line = None
    letter_str = ""
    while letter_line != "":
        letter_line = ref_letter.readline()
        letter_str = letter_str + letter_line

for name in name_list:
    edited_name = name.replace("\n", "")
    with open(f"Output/ReadyToSend/{edited_name}_letter.txt", "w") as letter_file:
        edited_letter_str = letter_str.replace("[name]", edited_name)
        letter_file.write(f"{edited_letter_str}")
