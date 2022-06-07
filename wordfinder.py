from random import choice as pick_word


class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self,file_path):
        self.file_path = file_path
        self.words_list = self.populate_words_list()
        self.message = print( f"{len(self.words_list)} words read")

    def random(self):
        return pick_word(self.words_list)

    def populate_words_list(self):
        file = open(self.file_path)
        word_list = []
        for line in file:

            word_list.append(line[:-1])
        return word_list
