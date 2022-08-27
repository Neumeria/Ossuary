import random
import sys
import time
import re
import os

os.system("cls")

print("Hello and Welcome!\n\n")

while True:
    name = input("Please Enter Your Name\n").strip()

    if name == '':
        print("\u001b[31mYou cannot insert blank lines as your name.\u001b[37m\n")
    else:
        break


def run(string):
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:,.;+-]')  
        if(regex.search(string) == None):
            segex = re.compile('^(?=.*[0-9]$)')
            if(segex.search(string) == None):
                print("\u001b[32mYour name is accepted.\u001b[37m\n")
            else:
                sys.exit("\u001b[31mYou cannot enter numbers in your name.\u001b[37m")
        else: 
            sys.exit("\u001b[31mYou cannot enter special characters in your name.\u001b[37m")


def newFunc1():
    print("\nWe offer two games to play! First is our quiz.\n")

    while True:
        gameChoice = input("Would You like to play? (YES/NO) (Y/N)\n").upper()

        if gameChoice == "YES" or gameChoice == "Y":
            break
        elif gameChoice == "NO" or gameChoice == "N":
            sys.exit("\u001b[33mThat's a shame! Have a nice day!\u001b[37m")
        else:
            print("Please Answer only Yes or No")
            continue

run(name)
newFunc1()

true = ["T", "t", "True"]
false = ["F", "f", "False"]
correct = 0 #Storing the correct answers

print ("\n\u001b[36mOK, " +  name +", let's get started. Remember, the following answers are only True or False.\u001b[37m")
time.sleep(2)

questions = ['Question 1', 'Question 2', 'Question 3', 'Question 4', 'Question 5', 'Question 6',
             'Question 7', 'Question 8', 'Question 9', 'Question 10', 'Question 11', 'Question 12', 'Question 13']
random.shuffle(questions)
question = 0
while question < 13:
    if questions[0] == 'Question 1':
        print ("\nParis is the captial of France.")
        choice = input(">>> ")
        if choice in true:
          correct += 1 #If correct, the user gets one point
          print("\u001b[32mYou have answered correctly!\u001b[37m\n")
        else:
          correct += 0
          print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
        del questions[0]
        question +=1
    elif questions[0] == 'Question 2':
        print ("\nEngland is not an island.")
        choice = input(">>> ")
        if choice in false:
          correct += 1
          print("\u001b[32mYou have answered correctly!\u001b[37m\n")
        else:
          correct += 0
          print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
        del questions[0]
        question +=1
    elif questions[0] == 'Question 3':
        print ("\nNorthern Ireland isn't part of Great Britian.")
        choice = input(">>> ")
        if choice in false:
          correct += 1
          print("\u001b[32mYou have answered correctly!\u001b[37m\n")
        else:
          correct += 0
          print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
        del questions[0]
        question +=1
    elif questions[0] == 'Question 4':
        print ("\nAndorra is between France and Spain.")
        choice = input(">>> ")
        if choice in true:
          correct += 1
          print("\u001b[32mYou have answered correctly!\u001b[37m\n")
        else:
          correct += 0
          print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
        del questions[0]
        question +=1
    elif questions[0] == 'Question 5':
        print ("\nIran use to be part of the Perisan Empire.")
        choice = input(">>> ")
        if choice in true:
          correct += 1
          print("\u001b[32mYou have answered correctly!\u001b[37m\n")
        else:
          correct += 0
          print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
        del questions[0]
        question +=1
    elif questions[0] == 'Question 6':
        print ("\nTurkmenistan isn't a real country.")
        choice = input(">>> ")
        if choice in false:
          correct += 1
          print("\u001b[32mYou have answered correctly!\u001b[37m\n")
        else:
          correct += 0
          print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
        del questions[0]
        question +=1
    elif questions[0] == 'Question 7':
        print ("\nVenice is also known as The Floating City.")
        choice = input(">>> ")
        if choice in true:
          correct += 1
          print("\u001b[32mYou have answered correctly!\u001b[37m\n")
        else:
          correct += 0
          print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
        del questions[0]
        question +=1
    elif questions[0] == 'Question 8':
        print ("\nSwitzerland is also known as Confoederatio Helvetica.")
        choice = input(">>> ")
        if choice in true:
          correct += 1
          print("\u001b[32mYou have answered correctly!\u001b[37m\n")
        else:
          correct += 0
          print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
        del questions[0]
        question +=1
    elif questions[0] == 'Question 9':
        print ("\nThe Hagia Sophia is considered as the epitome of Byzantine architecture.")
        choice = input(">>> ")
        if choice in true:
          correct += 1
          print("\u001b[32mYou have answered correctly!\u001b[37m\n")
        else:
          correct += 0
          print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
        del questions[0]
        question +=1
    elif questions[0] == 'Question 10':
        print ("\n'Lady with an Ermine' is a painting by Michelangelo.")
        choice = input(">>> ")
        if choice in false:
          correct += 1
          print("\u001b[32mYou have answered correctly!\u001b[37m\n")
        else:
          correct += 0
          print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
        del questions[0]
        question +=1
    elif questions[0] == 'Question 11':
        print ("\nJulius Caesar was stabbed 32 times.")
        choice = input(">>> ")
        if choice in false:
          correct += 1
          print("\u001b[32mYou have answered correctly!\u001b[37m\n")
        else:
          correct += 0
          print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
        del questions[0]
        question +=1
    elif questions[0] == 'Question 12':
        print ("\n'The Raven' is the most famous poem by Edgar Allan Poe.")
        choice = input(">>> ")
        if choice in true:
          correct += 1
          print("\u001b[32mYou have answered correctly!\u001b[37m\n")
        else:
          correct += 0
          print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
        del questions[0]
        question +=1
    elif questions[0] == 'Question 13':
        print ("\nJeanne d'Arc gained command over the armies of France at the age of 19.")
        choice = input(">>> ")
        if choice in false:
          correct += 1
          print("\u001b[32mYou have answered correctly!\u001b[37m\n")
        else:
          correct += 0
          print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
        del questions[0]
        question +=1

print ("\n\u001b[33mYou're finished, " + name +". You got", correct, "out of 13 correct.\u001b[37m")

wordList = [
"lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
 "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat", "hexakosioihexakontahexaphobia",
 "horse", "game", "hangman", "chicken", "bacon", "salmon", "android", "project",
 "university", "institution", "popcorn", "sophisticated", "easy", "melancholy",
 "effulgent", "program", "pseudocode", "vocabulary", "ambulance", "tiger"
           ]

guess_word = []
secretWord = random.choice(wordList)
length_word = len(secretWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []



def newFunc2():
    print("\u001b[36mNext up is the game of Hangman!\u001b[37m\n")

    while True:
        gameChoice = input("Would You like to play? (YES/NO) (Y/N)\n").upper()

        if gameChoice == "YES" or gameChoice == "Y":
            break
        elif gameChoice == "NO" or gameChoice == "N":
            sys.exit("\u001b[33mIt's alright, thank you for playing our quiz! Have a nice day!\u001b[37m")
        else:
            print("Please Answer only Yes or No")
            continue

newFunc2()



def change():

    for character in secretWord: # printing blanks for each letter in secret word
        guess_word.append("-")

    print("Ok, so the word you need to guess has", length_word, "characters")

    print("Be aware that You can enter only 1 letter from a-z\n\n")

    print_word_to_guess(guess_word)



def guessing():
    guess_taken = 1
    MAX_GUESS = 10
    print_guesses_taken(guess_taken, MAX_GUESS)

    while guess_taken < MAX_GUESS:


        guess = input("Pick a letter\n").lower()

        if not guess in alphabet:
            print("Enter a letter from a-z alphabet")
        elif guess in letter_storage:
            print("\u001b[34mYou have already guessed that letter!\u001b[37m")
        else: 

            letter_storage.append(guess)
            if guess in secretWord:
                print("\u001b[32mYou guessed correctly!\u001b[37m")
                for x in range(0, length_word):
                    if secretWord[x] == guess:
                        guess_word[x] = guess
                print_word_to_guess(guess_word)
                print_guesses_taken(guess_taken, MAX_GUESS)

                if not '-' in guess_word:
                    print("\u001b[32mCongratulations!\u001b[37m")
                    print("\u001b[32mYou won!\u001b[37m")
                    break
            else:
                print("\u001b[31mThe letter is not in the word. Try Again!\u001b[37m")
                guess_taken += 1
                print_guesses_taken(guess_taken, MAX_GUESS)
                if guess_taken == 10:
                    print("\u001b[31mSorry "+name+", you lost! :< The secret word was:- \u001b[37m",secretWord)
                    print("\u001b[31mGame Over!\u001b[37m")

def print_word_to_guess(letters):
    #Utility function to print the current word to guess
    print("Word to guess: {0}".format(" ".join(guess_word)))

def print_guesses_taken(current, total):
    #Prints how many chances the player has used
    print("You are on guess {0}/{1}.\n".format(current, total))

change()
guessing()
