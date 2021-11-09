import random

#making a collection of words
word_set = ["alaska", "alabama", "arizona", "arkansas", "california", "colorado", "connecticut", "delaware", "florida", "georgia", "hawaii", 
"idaho", "illinois", "indiana", "iowa", "kansas", "kentucky", "lousiana", "maine", "maryland", "massachusetts", "michigan", "minnesota", 
"mississippi", "missouri", "montana", "nebraska", "nevada", "new hampshire", "new jersey", "new mexico", "new york", "north carolina", "north dakota", 
"ohio", "oklahoma", "oregon", "pennsylvania", "rhode island", "south carolina", "south dakota", "tennessee", "texas", "utah", "vermont", "virginia", 
"washington", "west virginia", "wisconsin", "wyoming"]

#welcome the user and ask their name 
print("\nHello! Welcome to Hangman \n")

#asking for number of players
num_players = input("Are you a single player or multiplayer? Type in 'single' if you are a single player and 'multi' otherwise\n")

#if a single player, generate a random word.
if num_players == "single":
    word = random.choice(word_set)

#if multiplayer, ask for an input word
if num_players == "multi":
    word = input("Enter an U.S. state to be guessed:\n")
    #clearing the terminal so that the word inputted by the user isnt visible
    print(chr(27) + "[2J")

#get the lenght of the word to be guessed
word_len = len(word)

#the player has 5 more guesses than the length of the word 
guess_count = word_len + 5

print("\nYou have " + str(guess_count) + " turns to get the word right\n")

i = word_len
while i>0:
    print("_ ", end = '')
    i = i - 1

print("\n")

guessed = ""

while guess_count > 0 :
    guess = input("\nYou have " + str(guess_count) + " guesses left. Make your next guess: \n")
    guessed = guessed + guess
    for letter in word:
        if letter in guessed:
            print(letter+ " ", end = '')
        else:
            print("_ ", end = '')
        print("\n")

    guess_count = guess_count - 1





    

 
