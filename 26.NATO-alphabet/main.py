import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter your word:").upper()
coded_word = [nato_dict[letter] for letter in word]
print(coded_word)