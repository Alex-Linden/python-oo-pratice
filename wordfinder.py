from random import choice as pick_word


class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self,file_path):
        """creates a list of words from a file path and a prints number of words in the list"""
        self.file_path = file_path
        self.words_list = self.get_words_list()
        print( f"{len(self.words_list)} words read")

    def random(self):
        """selects a random word from a list of words in the instance"""
        return pick_word(self.words_list)

    def get_words_list(self):
        """returns a list of words from the file_path given at creatation"""
        file = open(self.file_path)
        return [line.strip() for line in file]


class SpecialWordFinder(WordFinder):
    """This sub class removes list items that start with a # or are a blank space"""

    def get_words_list(self):
        """returns a list of words from the file_path given at creatation """
        return [item for item in super().get_words_list()
            if not item == '' and not item.startswith('#')]