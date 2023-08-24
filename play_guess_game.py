from guess_game import GuessGame

def main():
    print("Welcome to Guess the Number game!")

    play_again = True
    while play_again:
        game = GuessGame()
        attempts = 0

        while True:
            guess = input("Enter your guess (4-digit number or 'q' to quit): ")
            if guess.lower() == 'q':
                print(f"The target number was: {game.target_number}")
                break

            if len(guess) != 4 or not guess.isdigit():
                print("Invalid input. Please enter a 4-digit number or 'q' to quit.")
                continue

            attempts += 1
            result = game.check_guess(int(guess))
            print(result)

            if "Congratulations" in result:
                print(f"You guessed the number in {attempts} attempts!")
                break

        play_again = input("Do you want to play again? (yes/no): ").lower() == 'yes'

if __name__ == "__main__":
    main()
