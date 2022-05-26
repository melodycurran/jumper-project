from game.terminal_service import TerminalService

class Guesser:
    """The person who guesses the random word letter by letter.
    
    The responsibility of the guesser is to guess the word letter by letter.

    Attributes:
        word (str): The random word from the list
    """

    def __init__(self):
        """Constructs a new Guesser.

        Args:
            self (Guesser): An instance of Guesser.
        """
        self.terminal = TerminalService()

    def _get_input(self):
        """Asks user for their guess.

         Args:
            self (Guesser): An instance of Guesser.
        """
        self.input = self.terminal.read_text('Guess a letter [a-z]: ')