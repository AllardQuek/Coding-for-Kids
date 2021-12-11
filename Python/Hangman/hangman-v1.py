# Welcome the user
name = input("Player name: ")
print("Hello,", name, "Time to play Hangman!")
print()
print("Start guessing...")

# Set the secret word to be guessed
word = 'secret'

# Create a variable to keep track of guesses player has made
guesses = set()

# Set number of chances
chances = 10

# Set guessed variable to False
guessed = False

# Continue playing if player still has chances left
while chances > 0:
    # Print current progress 
    for char in word:
        print(char, end=" ") if char in guesses else print('_', end=" ")
    print()
        
    # Ask player to make a guess
    guess = input("guess a character: ")

    # Add the player's guess to the list of guesses
    guesses.add(guess)

    # If guess is wrong, number of chances decrease
    if guess not in word:
        chances -= 1
        print('Wrong')
        print('You have', chances, 'more chances to guess')
        continue
    
    # If guess is correct, check if game has been won
    if set(word).issubset(guesses):
        guessed = True
        print(f'You Won, congratulations! The word was {word}.')
        break

if not guessed:
    print('You Lose')
