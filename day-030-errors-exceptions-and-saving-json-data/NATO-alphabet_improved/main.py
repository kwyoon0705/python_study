import pandas

alphabet_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in alphabet_data_frame.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_word = [alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_word)


generate_phonetic()
