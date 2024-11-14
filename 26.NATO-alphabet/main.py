import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

def nato_generator():
    word = input("Enter your word:").upper()
    try:
        coded_word = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in alphabet please.")
    else:
        print(coded_word)
    finally:
        nato_generator()

nato_generator()
