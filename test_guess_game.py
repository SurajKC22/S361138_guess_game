#import framework 'unittest'
import unittest
from guess_game import GuessGame #import the guess_game directory

class TestGuessGame(unittest.TestCase):
    def test_generate_random_number(self): 
        # test if the generated random number is within the specified range (1000 to 9999)
        game = GuessGame()  # create an instance of the game
        number = game.generate_random_number()  # generate a random number
        self.assertTrue(1000 <= number <= 9999)  # check if the number is within the expected range

def test_check_guess_correct(self):
        # Test if the correct guess is detected and congratulated
        game = GuessGame()  # Create an instance of the game
        game.target_number = 1234  # Set the target number
        result = game.check_guess(1234)  # Check the correct guess
        self.assertEqual(result, "Congratulations! You guessed the right number.")  # Check if result matches expected
        
def test_check_guess_incorrect(self):
        # Test if an incorrect guess provides the appropriate feedback
        game = GuessGame()  # Create an instance of the game
        game.target_number = 1234  # Set the target number
        result = game.check_guess(4321)  # Check an incorrect guess
        self.assertIn("circle(s) and", result)  # Check if feedback contains the expected string
        
def test_check_guess_feedback(self):
        # Test if feedback is provided for an incorrect guess
        game = GuessGame()  # Create an instance of the game
        game.target_number = 1234  # Set the target number
        result = game.check_guess(5678)  # Check an incorrect guess
        self.assertIn("circle(s) and", result)  # Check if feedback contains the expected string
def test_quit_game(self):
        # Test if quitting the game is handled correctly
        game = GuessGame()  # Create an instance of the game
        game.target_number = 1234  # Set the target number
        result = game.check_guess("q")  # Simulate quitting the game
        self.assertEqual(result, "You quit the game. The target number was: 1234")  # Check if result matches expected

def test_play_game_correct_guess(self):
        # Test playing the game with a correct guess
        game = GuessGame()  # Create an instance of the game
        game.target_number = 1234  # Set the target number
        result = game.play_game([1234])  # Provide a list of guesses for testing
        self.assertEqual(result, "Congratulations! You guessed the number in 1 attempt.")  # Check if result matches expected
def test_play_game_multiple_attempts(self):
        # Test playing the game with multiple attempts
        game = GuessGame()  # Create an instance of the game
        game.target_number = 5678  # Set the target number
        result = game.play_game([1234, 5678, 9876])  # Provide a list of guesses for testing
        self.assertEqual(result, "Congratulations! You guessed the number in 2 attempts.")  # Check if result matches expected
if __name__ == "__main__":
    unittest.main()
