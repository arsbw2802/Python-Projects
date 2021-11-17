# @author Aarushi Biswas
# Level of difficulty of project: Basic
# Project: Hangman game
# Decription:


import random
import sys
import pandas
 
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
len_guessed = 0
guessed_word = ""
finished = None
 
while guess_count > 0 :
   guess = input("\nYou have " + str(guess_count) + " guesses left. Make your next guess: ")
   print("Your guesses till now have been: " + guessed)
   guessed = guessed + guess
   for letter in word:
       if letter in guessed:
           print(letter + " ", end = "")
           if(letter not in guessed_word):
               guessed_word += letter
       else:
           print("_ ", end = "")
       if(len(guessed_word) == word_len):
           print("\nYou have guessed it correctly!\n")
           finished = True
           #print(str(word_len) + " " + str(len(guessed_word)) + " " + guessed_word)
           break
   #print(guessed_word)
   print("\n")
   guess_count = guess_count - 1
   if finished == True:
       break
 
if(guess_count == 0):
   print("You have ran out of guesses! Thanks for playing\n")
 
 
yn = input("Do you want to play again? Y/N: ")
 
if yn == "Y":
   #run()#restart
   print("restart")
elif yn == "N":
   print("Thanks for playing")
   sys.exit()

