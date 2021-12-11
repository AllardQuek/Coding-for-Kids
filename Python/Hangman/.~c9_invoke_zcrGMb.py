"""
Hangman Game: Version 2

TODO:
1. Break down program into functions
2. Add word list. (animals.txt)

Optional
3. Check if user inputs only 1 character
4. Check if user has already guessed a letter
"""


# Import random library for choosing random word
import random

# Specify name of file containing list of possible words
WORD_LIST_FILENAME = "animals.txt"


def start_game():
    guesses, chances, name = initialise_game()
    word_list = load_words()
    word = choose_word(word_list)
    print("Start guessing!")

    
    # Continue playing if player still has chances left
    while chances > 0:
        # Print current progress 
        for char in word:
            print(char, end=" ") if char in guesses else print('_', end=" ")
        print("\n\n")
            
        # Ask player to make a guess
        guess = input("guess a character: ")
    
        # Add the player's guess to the list of guesses
        guesses.add(guess)
    
        # If guess is wrong, number of chances decrease
        if guess not in word:
            chances -= 1
            print('Wrong! You have', chances, 'more chances to guess')
            continue
        
        # If guess is correct, check if game has been won
        if set(word).issubset(guesses):
            guessed = True
            print(f'You Won, congratulations! The word was {word}.')
            return
    
    print(f'Sorry, you lose! The word was {word}')
    

def initialise_game():
    # Create a variable to keep track of guesses player has made
    guesses = set()
    
    # Set number of chances
    chances = 10
    
    # Welcome player
    name = input("Player name: ")
    print("Hello,", name, "Time to play Hangman!")

    return guesses, chances, name
    

def load_words():
    print("Loading word list...")
    with open("animals.txt", "r") as f:
        word_list = [word.rstrip() for word in f]
        return word_list
        

def choose_word(word_list):
    print("Choosing word...")
    return random.choice(word_list)

if __name__ == "__main__":
    start_game()
