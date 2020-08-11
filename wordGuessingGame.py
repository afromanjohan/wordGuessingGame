# Import libraries
from PyDictionary import PyDictionary
dictionary = PyDictionary()
from random_words import RandomWords
r = RandomWords()

# Select random word for the game
word = r.random_word()

# Create variables to keep track of game state
count_guesses = 0
previous_guesses = []


# Helping function to sort list of guesses and inform about the status of last guess
def guess_is_before_solution(guess):
    list = [word]
    list.append(guess)
    list.sort()
    if list.pop() == guess:
        previous_guesses.append((guess, "after"))
        return guess + " is after solution"
    previous_guesses.append((guess, "before"))
    return guess + " is before solution"

# Main game loop
print("Type a suggestion to get started: ")
while True:
    if len(previous_guesses) > 0:
        previous_guesses.sort()
        for i in range(len((previous_guesses))):
            print(previous_guesses[i])
    userSuggestion = input()
    if userSuggestion == "1":
        print("The word was: " + word)
        break
    elif not dictionary.meaning(userSuggestion, True):
        print("This is not a word, try again, type '1' to give up.")
    elif userSuggestion == word:
        count_guesses += 1
        print("You won! The word was: " + str(word) + ", you got it after: " + str(count_guesses) + " amount of guesses.")
        break
    else:
        count_guesses += 1
        print(guess_is_before_solution(userSuggestion) + ", guess number: " + str(count_guesses))
