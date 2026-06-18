import random

class HangmanGame:
    """
    A class to represent the Hangman Game logic.
    """
    def __init__(self, word_list=None):
        if word_list is None:
            self.word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "watermelon"]
        else:
            self.word_list = word_list
        
        self.secret_word = ""
        self.guessed_letters = set()
        self.remaining_chances = 0
        self.game_over = False
        self.won = False

    def start_new_game(self):
        """Initializes a new game session."""
        self.secret_word = random.choice(self.word_list).lower()
        self.guessed_letters = set()
        # Requirement: length of the word + 2 chances
        self.remaining_chances = len(self.secret_word) + 2
        self.game_over = False
        self.won = False
        return self.secret_word

    def get_display_word(self):
        """Returns the word with underscores for unguessed letters."""
        return " ".join([char if char in self.guessed_letters else "_" for char in self.secret_word])

    def guess(self, letter):
        """Processes a letter guess."""
        letter = letter.lower()
        
        if self.game_over:
            return False, "Game is already over."
        
        if not letter.isalpha() or len(letter) != 1:
            return False, "Invalid input. Please enter a single letter."
        
        if letter in self.guessed_letters:
            return False, f"You already guessed '{letter}'."
        
        self.guessed_letters.add(letter)
        
        if letter in self.secret_word:
            if all(char in self.guessed_letters for char in self.secret_word):
                self.game_over = True
                self.won = True
                return True, "Correct! You've guessed the word!"
            return True, "Correct guess!"
        else:
            self.remaining_chances -= 1
            if self.remaining_chances <= 0:
                self.game_over = True
                self.won = False
                return False, f"Wrong guess. Game over! The word was '{self.secret_word}'."
            return False, "Wrong guess."

    def get_status(self):
        """Returns the current state of the game."""
        return {
            "display_word": self.get_display_word(),
            "remaining_chances": self.remaining_chances,
            "guessed_letters": sorted(list(self.guessed_letters)),
            "game_over": self.game_over,
            "won": self.won
        }

def main():
    print("--- Welcome to the Hangman Game ---")
    game = HangmanGame()
    secret = game.start_new_game()
    
    print(f"I have picked a secret fruit. It has {len(secret)} letters.")
    print(f"You have {game.remaining_chances} chances to guess it.")

    while not game.game_over:
        status = game.get_status()
        print(f"\nWord: {status['display_word']}")
        print(f"Chances left: {status['remaining_chances']}")
        print(f"Guessed so far: {', '.join(status['guessed_letters'])}")
        
        user_input = input("Guess a letter: ").strip()
        if not user_input:
            continue
            
        success, message = game.guess(user_input)
        print(message)

    if game.won:
        print(f"\nCongratulations! You won! The word was '{game.secret_word}'.")
    else:
        print(f"\nBetter luck next time! The word was '{game.secret_word}'.")

if __name__ == "__main__":
    main()
