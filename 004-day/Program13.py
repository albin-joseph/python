# Write a program to find out a word randomly from a string.
#To do this program we will use List, random and a string method split and len.

import random

sentence = input("Please enter a senetence: ")
words = sentence.split(" ")
words_length = len(words)
if words_length > 0:
    random_int = random.randint(0, words_length-1)
    print(words[random_int])
else:
    print("Please try with a valid sentence.")
    
print("We can write this program by using random choice method also")
print(random.choice(words))
