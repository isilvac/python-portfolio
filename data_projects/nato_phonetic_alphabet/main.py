import pandas


# 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_data = pandas.read_csv("data/nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}


# 2. Create a list of the phonetic code words from a word that the user inputs.
def translate():
    word = input("Enter a word: ").upper()
    try:
        spelled_word = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        translate()
    else:
        print(spelled_word)


translate()
