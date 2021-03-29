# Python custom dictionary class with various methods.

import random
import math


class Dictionary:
    """
    A dictionary object

    Attributes:
    ----------
    dictionary
        A dictionary that supports key:value pairs in the form of Word:Definition

    Methods:
    --------
    random_word()
        Returns a random word and its definition
    stats()
        Returns number of words in the dictionary
    add_word(word="str", definition="str")
        Adds a word and definition to the dictionary
    remove_word(word="str")
        Removes a word and definition from the dictionary
    edit_definition(word="str", new_definition="str")
        Edit definition of a word in the dictionary
    print_dictionary()
        Returns all words and their definitions from the dictionary
    average_word_size()
        Returns the average word size
    """

    def __init__(self):
        self.dictionary = {}

    def __repr__(self):
        return f'A dictionary with {self.stats()} entries.'

    def random_word(self):
        """
        Gives the user a random word.
        :return: A random word and its definition.
        :rtype: str
        """
        word, definition = random.choice(list(self.dictionary.items()))
        return f'Word: {word}\nDefinition: {definition}\n'

    def stats(self):
        """
        Show the number of words in the dictionary.
        :return: Number of words in the dictionary.
        :rtype: int
        """
        return len(self.dictionary)

    def add_word(self, word, definition):
        """
        Add a new word and definition to the dictionary.
        :param word:
        :type word: str
        :param definition:
        :type definition: str
        :return: None
        :rtype: None
        """
        self.dictionary[word] = definition

    def remove_word(self, word):
        """
        Remove a word from the dictionary.
        :param word: Word a used wishes to remove from the dictionary.
        :type word: str
        :return: None
        :rtype: None
        """
        if word in self.dictionary:
            self.dictionary.pop(word)
        else:
            raise Exception(f'"{word}" is not in the dictionary.')

    def edit_definition(self, word, new_definition):
        """
        Edit the definition of an existing word.
        :param word: Word a user wishes to change the definition of.
        :type word: str
        :param new_definition: The new definition.
        :type new_definition: str
        :return: None
        :rtype: None
        """
        self.dictionary[word] = new_definition

    def print_dictionary(self):
        """
        Returns the dictionary words and their definitions in a list.
        :return: Returns all dictionary words and their definitions in a list.
        :rtype: list
        """
        for word, definition in self.dictionary.items():
            yield f'Word: {word}\nDefinition: {definition}\n'

    def average_word_size(self):
        """
        Returns the average word size of all words rounded down.
        :return: Returns int of average dictionary key size
        :rtype: int
        """
        total = 0
        for key in self.dictionary:
            total += len(key)
        return math.floor(total / dictionary.stats())


dictionary = Dictionary()