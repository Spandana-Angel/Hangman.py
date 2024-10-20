import random

def get_word():
    words = ['python', 'java', 'kotlin', 'javascript', 'hangman', 'programming']
    return random.choice(words)

def display_game(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    word = get_word()
    guessed_letters = []
    attempts = 6  # Number of wrong attempts before the game is over
    word_guessed = False
    
    print("Welcome to Hangman!")
    
    while attempts > 0 and not word_guessed:
        print(f"\nYou have {attempts} attempts remaining.")
        print("Word: ", display_game(word, guessed_letters))
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Wrong guess! {guess} is not in the word.")
            attempts -= 1
        
        if '_' not in display_game(word, guessed_letters):
            word_guessed = True

    if word_guessed:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nGame over! The word was: {word}")

if __name__ == '__main__':
    hangman()
