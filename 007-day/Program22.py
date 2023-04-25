# create sample app for demonstarte decision make and looping statements in python.
#Let's do the hangman project.
import random
#Create word list
words = ["albin", "peacock", "orange", "apple"]

#Randomly select a word from word list
selected_word = random.choice(words)
print(selected_word)

word_length = len(selected_word)

display = []

for _ in range(word_length):
    display.append("-")

print(display)

for _ in range(word_length):
    #Guess a letter
    guess = input("Guess a letter: ").lower()

    #check the guess letter in the words choosen
    for position in range(word_length):
        letter = selected_word[position]
        if letter == guess:
            display[position] = letter

    print(display)
print(f"final guess: ${display}")