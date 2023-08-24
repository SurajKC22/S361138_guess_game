import random

class GuessGame:
    def __init__(self):
        self.target_number = self.generate_random_number()

    def generate_random_number(self):
        return random.randint(1000, 9999)

    def check_guess(self, guess):
        target_str = str(self.target_number)
        guess_str = str(guess)

        if guess_str == target_str:
            return "Congratulations! You guessed the number."

        circles = sum(1 for i, j in zip(guess_str, target_str) if i == j)
        xs = sum(min(guess_str.count(digit), target_str.count(digit)) for digit in set(guess_str)) - circles

        return f"{circles} circle(s) and {xs} x(s)"
