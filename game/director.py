from game.word import Word
from game.terminal_service import TerminalService
from game.guesser import Guesser

class Director:
    """The person who directs the game.
    
    Attributes:

        _is_playing(boolean): Directs the loop of the game.
        _random_word(str): Creates a new random word from the list.
        _terminal : Calls the terminal service.
        guesser: Calls the guesser class
        hide(str): Hides the word through underscore.
        wrong_guess(list): Counts the player's wrong guesses.
        word(str): Stores the word generated called through _random_word.
        parachute(list): Draws the parachute.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._random_word = Word()
        self._terminal = TerminalService()
        self.guesser = Guesser()
        self.hide = ""
        self.wrong_guess = []
        self.word = ""
        self.parachute = [
            '   _____',
            '  /_____\\',
            '  \     /',
            '   \   /',
            '     0',
            '    /|\\',
            '    / \\',
            '',
            ' ^^^^^^^^^^'
        ]

    def _start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_random_word()
            self._hide_word()
            self._draw_parachute()

            # If the player guessed incorrectly four times, it will terminate the game.
            if len(self.wrong_guess) ==  4:
                self._is_playing = False

            # If the player guessed the word, this will terminate the game.
            elif self.hide == self.word:
                self._is_playing = False
            else:
                self._get_inputs()
                self._do_updates()


    def _get_random_word(self):
        """Generate random word and hide it from the player.
        
        Args:
            self (Director): an instance of Director.
        """
        self.word = self._random_word.get_word()

    def _hide_word(self):

        # Gets the input of the player which is a letter
        guess = self.guesser.input
        
        # If it's the start of the game and player hasn't entered anything obviously,
        # it will only show the word hidden by replacing the letters with underscores.
        if guess == "":
            self.hide = "_" * len(self.word)
            self._terminal.write_text(f'The word is: {self.hide}')

        # The letter guessed is in self.word, then we'll look for the index of that letter within self.word.
        elif guess in self.word:

            # We'll store the index in i
            i = self.word.index(guess)

            # There are more than one letter that are the same in self.word, then, we'll look at the last index.
            if guess in self.hide:
                i = self.word.rindex(guess)

            # This will print the correct letter guessed while hiding the rest of the letters
            self.hide = self.hide[:i] + self.word[i] + self.hide[i + 1:]
            self._terminal.write_text(f'The word is: {self.hide}')
            
            # If player guessed all the letters, then this will print
            if self.hide == self.word:
                self._terminal.write_text('Congratulations! You guessed it right!')

        # If player guessed 4 times incorrectly, this will print.
        elif len(self.wrong_guess) ==  4:
            self._terminal.write_text(f'The word is: {self.word}')
            self._terminal.write_text('You lost the game.')
        
        # If player guessed the letter incorrectly, this will only print whatever is stored in self.hide
        else:
            self._terminal.write_text(f'The word is: {self.hide}')

    def _draw_parachute(self):
        """Prints the parachute on the terminal.
        
        Args:
            self (Director): an instance of Director
        """
        for line in self.parachute:
            self._terminal.write_text(line)

    def _get_inputs(self):
        """Get input from the user about their guess.

        Args:
            self (Director): An instance of Director.
        """
        self.guesser._get_input()

    def _do_updates(self):
        """Updates when the player guesses the letter right or not.

        Args:
            self (Director): An instance of Director.
        """
        if self.guesser.input in self.word:
            pass

        else:
            # This will add all the wrong guess the player made
            self.wrong_guess.append(self.guesser.input)

            # If the player guessed four times incorrectly,
            if len(self.wrong_guess) == 4:
                # The head of the hangman will be replaced by x
                self.parachute[1] = '     x'
                # This will delete the other part of the parachute
                self.parachute.pop(0)
            else:
                self.parachute.pop(0)
                


        


