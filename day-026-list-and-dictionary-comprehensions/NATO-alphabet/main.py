import pandas

alphabet_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in alphabet_data_frame.iterrows()}

word = input("Enter a word: ").upper()
output_word = {alphabet_dict[letter] for letter in word}
print(output_word)