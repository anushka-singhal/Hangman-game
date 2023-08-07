import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "language", "openai", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    while True:
        print("\n" + display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word_to_guess:
            print("Correct!")
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
            if attempts == 0:
                print("Game over! The word was:", word_to_guess)
                break
        
        if "_" not in display_word(word_to_guess, guessed_letters):
            print("Congratulations! You've guessed the word:", word_to_guess)
            break

if __name__ == "__main__":
    hangman()
