from random import choice as pick_word
LETTERS = 'abcdefghijklmnopqrstuvwxyz'


class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self,file_path):
        """creates a list of words from a file path and a prints number of words in the list"""
        self.file_path = file_path
        self.words_list = self.get_words_list()
        print( f"{len(self.words_list)} words read")

    def random(self):
        """selects a random word from the word list in the instance"""
        return pick_word(self.words_list)

    def get_words_list(self):
        """called when the instance is created to get words_list from file"""
        file = open(self.file_path)
        return [line.strip() for line in file]


class SpecialWordFinder(WordFinder):
    """This sub class accounts for lists that don't start with a letter and doesn't include them"""

    def __init__(self, file_path):
        """creates a list of words from a file path and a prints number of words in the list"""
        super().__init__(file_path)

    def get_words_list(self):
        """called when the instance is created to get words_list from file"""
        file = open(self.file_path)
        return [line.strip() for line in file if line[0].lower() in LETTERS ]