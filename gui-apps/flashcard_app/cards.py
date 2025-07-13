import random
import pandas


class Cards:

    def __init__(self):
        with open(file="data/french_words.csv") as file:
            data = pandas.read_csv(file)
        langs = [key for key in data.keys()]
        self.lang1 = langs[0]
        self.lang2 = langs[1]
        self.words = data.to_dict(orient="records")
        self.current_card = self.get_random_word()
        self.unknown_words = []

    def get_random_word(self):
        return random.choice(self.words)

    def remove_word(self, item):
        index = self.words.index(item)
        self.words.pop(index)

    def save_words(self):
        pandas.DataFrame(self.unknown_words).to_csv("data/words_to_learn.csv", index=False)
