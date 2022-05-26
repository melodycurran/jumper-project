import random

class Word:
    """The random word.

    The responsibility of Word is to generate random word from the list.

    Attributes:
        _words_list (str) / (list): The list of words the player will guess.
        _random (int): Generates random number from zero to the length of the list
    """
    def __init__(self):
        """Constructs new Word.

        Args:
            self (Word): an instance of Word.
        """
        self._words_list = ["abbreviation", "cognitive", "allusion", "casket", "concavity", 
        "buoyancy", "comatic", "mercurial", "contempt", "aphasia", "disney", "lobotomy", "priceless",
        "estate", "taxation", "watermelon", "spaceship", "subsequential", "odyssey", "fortune",
        "village", "carnivore", "elephant", "foliage", "microwave", "halibut", "sunshine", "velocity",
        "exterior", "inferior", "firmament", "elaborate"]
        # Some words are from https://www.merriam-webster.com/

        self._random = random.randint(0, (len(self._words_list) - 1))
        self._get_random_word = ""

    def get_word(self):
        """Picks random word from the list
        
        Args: 
            self (Word): an instance of Word.
        """
        self._get_random_word = self._words_list[self._random]

        return self._get_random_word