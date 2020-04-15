#!C:/Users/chaos/AppData/Local/Programs/Python/Python37/python.exe
import random
import sys
import time
import re
import os
import tkinter as tk
from tkinter import ttk

print("Content-Type: text/javascript")
print()

os.system("cls")

print("Hello and Welcome!\n\n")

win = tk.Tk()
win.title("Python GUI App")  
lbl = ttk.Label(win, text = "Enter the name:").grid(column = 0, row = 0)  
def click():
    print("Hi, " + name.get())
    win.destroy()
name = tk.StringVar()
nameEntered = ttk.Entry(win, width = 35,justify='center', textvariable = name).grid(column = 0, row = 1)
button = ttk.Button(win, text = "Submit", command = click).grid(column = 1, row = 1)  
win.mainloop()

while True:
    #name = input("Please Enter Your Name\n").strip()

    if name.get() == '':
        print("\u001b[31mYou cannot insert blank lines as your name.\u001b[37m\n")
        sys.exit()
    else:
        break


def run(string):
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:,.;+-]')  
        if(regex.search(string) == None):
            segex = re.compile('^(?=.*[0-9]$)')
            if(segex.search(string) == None):
                print("\u001b[32mYour name is accepted.\u001b[37m\n")
            else:
                print("\u001b[31mYou cannot enter numbers in your name.\u001b[37m")
                sys.exit()
        else: 
            print("\u001b[31mYou cannot enter special characters in your name.\u001b[37m")
            sys.exit()

run(name.get())

print("We offer you a game of Quiz!")
print("Would You like to play?\n")

def yes():
    w.destroy()

def no():
    print("\u001b[33mThat's a shame! Have a nice day!\u001b[37m")
    sys.exit()

w = tk.Tk()
w.title("Python GUI App")  
lbl = ttk.Label(w, text = "Enter the option:").grid(column = 0, row = 0)   
button1 = ttk.Button(w, text = "Yes", command = yes).grid(column = 1, row = 1)  
button2 = ttk.Button(w, text = "No", command = no).grid(column = 2, row = 1)  
w.mainloop()

#true = ["T", "t", "True"]
#false = ["F", "f", "False"]

print ("\u001b[36mOK " +  name.get() +", let's get started. Remember, the following answers are only True or False.\u001b[37m\n")
time.sleep(2)

correct = 0 #Storing the correct answers
questions = ['Question 1', 'Question 2', 'Question 3', 'Question 4', 'Question 5', 'Question 6',
             'Question 7', 'Question 8', 'Question 9', 'Question 10', 'Question 11', 'Question 12', 'Question 13']
random.shuffle(questions)
question = 0
while question < 13:
    if questions[0] == 'Question 1':
        print ("\nParis is the captial of France.")
        #choice = input(">>> ")
        def t1():
            global correct
            correct=correct+1 #If correct, the user gets one point
            print("\u001b[32mYou have answered correctly!\u001b[37m\n")
            q.destroy()
        def f1():
            #correct += 0
            print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
            q.destroy()
        q = tk.Tk()
        q.title("Python GUI App")  
        lbl = ttk.Label(q, text = "Enter the option:").grid(column = 0, row = 0)   
        b1 = ttk.Button(q, text = "True", command = t1).grid(column = 1, row = 1)  
        b2 = ttk.Button(q, text = "False", command = f1).grid(column = 2, row = 1)  
        q.mainloop()
        del questions[0]
        question +=1
    elif questions[0] == 'Question 2':
        print ("\nEngland is not an island.")
        #choice = input(">>> ")
        def f2():
            global correct
            correct=correct+1
            print("\u001b[32mYou have answered correctly!\u001b[37m\n")
            q.destroy()
        def t2():
            #correct += 0
            print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
            q.destroy()
        q = tk.Tk()
        q.title("Python GUI App")  
        lbl = ttk.Label(q, text = "Enter the option:").grid(column = 0, row = 0)   
        b1 = ttk.Button(q, text = "True", command = t2).grid(column = 1, row = 1)  
        b2 = ttk.Button(q, text = "False", command = f2).grid(column = 2, row = 1)  
        q.mainloop()
        del questions[0]
        question +=1
    elif questions[0] == 'Question 3':
        print ("\nNorthern Ireland isn't part of Great Britian.")
        #choice = input(">>> ")
        def f3():
            global correct
            correct=correct+1
            print("\u001b[32mYou have answered correctly!\u001b[37m\n")
            q.destroy()
        def t3():
            #correct += 0
            print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
            q.destroy()
        q = tk.Tk()
        q.title("Python GUI App")  
        lbl = ttk.Label(q, text = "Enter the option:").grid(column = 0, row = 0)   
        b1 = ttk.Button(q, text = "True", command = t3).grid(column = 1, row = 1)  
        b2 = ttk.Button(q, text = "False", command = f3).grid(column = 2, row = 1)  
        q.mainloop()
        del questions[0]
        question +=1
    elif questions[0] == 'Question 4':
        print ("\nAndorra is between France and Spain.")
        #choice = input(">>> ")
        def t4():
            global correct
            correct=correct+1
            print("\u001b[32mYou have answered correctly!\u001b[37m\n")
            q.destroy()
        def f4():
            #correct += 0
            print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
            q.destroy()
        q = tk.Tk()
        q.title("Python GUI App")  
        lbl = ttk.Label(q, text = "Enter the option:").grid(column = 0, row = 0)   
        b1 = ttk.Button(q, text = "True", command = t4).grid(column = 1, row = 1)  
        b2 = ttk.Button(q, text = "False", command = f4).grid(column = 2, row = 1)  
        q.mainloop()
        del questions[0]
        question +=1
    elif questions[0] == 'Question 5':
        print ("\nIran use to be part of the Perisan Empire.")
        #choice = input(">>> ")
        def t5():
            global correct
            correct=correct+1
            print("\u001b[32mYou have answered correctly!\u001b[37m\n")
            q.destroy()
        def f5():
            #correct += 0
            print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
            q.destroy()
        q = tk.Tk()
        q.title("Python GUI App")  
        lbl = ttk.Label(q, text = "Enter the option:").grid(column = 0, row = 0)   
        b1 = ttk.Button(q, text = "True", command = t5).grid(column = 1, row = 1)  
        b2 = ttk.Button(q, text = "False", command = f5).grid(column = 2, row = 1)  
        q.mainloop()
        del questions[0]
        question +=1
    elif questions[0] == 'Question 6':
        print ("\nTurkmenistan isn't a real country.")
        #choice = input(">>> ")
        def f6():
            global correct
            correct=correct+1
            print("\u001b[32mYou have answered correctly!\u001b[37m\n")
            q.destroy()
        def t6():
            #correct += 0
            print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
            q.destroy()
        q = tk.Tk()
        q.title("Python GUI App")  
        lbl = ttk.Label(q, text = "Enter the option:").grid(column = 0, row = 0)   
        b1 = ttk.Button(q, text = "True", command = t6).grid(column = 1, row = 1)  
        b2 = ttk.Button(q, text = "False", command = f6).grid(column = 2, row = 1)  
        q.mainloop()
        del questions[0]
        question +=1
    elif questions[0] == 'Question 7':
        print ("\nVenice is also known as The Floating City.")
        #choice = input(">>> ")
        def t7():
            global correct
            correct=correct+1
            print("\u001b[32mYou have answered correctly!\u001b[37m\n")
            q.destroy()
        def f7():
            #correct += 0
            print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
            q.destroy()
        q = tk.Tk()
        q.title("Python GUI App")  
        lbl = ttk.Label(q, text = "Enter the option:").grid(column = 0, row = 0)   
        b1 = ttk.Button(q, text = "True", command = t7).grid(column = 1, row = 1)  
        b2 = ttk.Button(q, text = "False", command = f7).grid(column = 2, row = 1)  
        q.mainloop()
        del questions[0]
        question +=1
    elif questions[0] == 'Question 8':
        print ("\nSwitzerland is also known as Confoederatio Helvetica.")
        #choice = input(">>> ")
        def t8():
            global correct
            correct=correct+1
            print("\u001b[32mYou have answered correctly!\u001b[37m\n")
            q.destroy()
        def f8():
            #correct += 0
            print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
            q.destroy()
        q = tk.Tk()
        q.title("Python GUI App")  
        lbl = ttk.Label(q, text = "Enter the option:").grid(column = 0, row = 0)   
        b1 = ttk.Button(q, text = "True", command = t8).grid(column = 1, row = 1)  
        b2 = ttk.Button(q, text = "False", command = f8).grid(column = 2, row = 1)  
        q.mainloop()
        del questions[0]
        question +=1
    elif questions[0] == 'Question 9':
        print ("\nThe Hagia Sophia is considered as the epitome of Byzantine architecture.")
        #choice = input(">>> ")
        def t9():
            global correct
            correct=correct+1
            print("\u001b[32mYou have answered correctly!\u001b[37m\n")
            q.destroy()
        def f9():
            #correct += 0
            print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
            q.destroy()
        q = tk.Tk()
        q.title("Python GUI App")  
        lbl = ttk.Label(q, text = "Enter the option:").grid(column = 0, row = 0)   
        b1 = ttk.Button(q, text = "True", command = t9).grid(column = 1, row = 1)  
        b2 = ttk.Button(q, text = "False", command = f9).grid(column = 2, row = 1)  
        q.mainloop()
        del questions[0]
        question +=1
    elif questions[0] == 'Question 10':
        print ("\n'Lady with an Ermine' is a painting by Michelangelo.")
        #choice = input(">>> ")
        def f10():
            global correct
            correct=correct+1
            print("\u001b[32mYou have answered correctly!\u001b[37m\n")
            q.destroy()
        def t10():
            #correct += 0
            print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
            q.destroy()
        q = tk.Tk()
        q.title("Python GUI App")  
        lbl = ttk.Label(q, text = "Enter the option:").grid(column = 0, row = 0)   
        b1 = ttk.Button(q, text = "True", command = t10).grid(column = 1, row = 1)  
        b2 = ttk.Button(q, text = "False", command = f10).grid(column = 2, row = 1)  
        q.mainloop()
        del questions[0]
        question +=1
    elif questions[0] == 'Question 11':
        print ("\nJulius Caesar was stabbed 32 times.")
        #choice = input(">>> ")
        def f11():
            global correct
            correct=correct+1
            print("\u001b[32mYou have answered correctly!\u001b[37m\n")
            q.destroy()
        def t11():
            #correct += 0
            print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
            q.destroy()
        q = tk.Tk()
        q.title("Python GUI App")  
        lbl = ttk.Label(q, text = "Enter the option:").grid(column = 0, row = 0)   
        b1 = ttk.Button(q, text = "True", command = t11).grid(column = 1, row = 1)  
        b2 = ttk.Button(q, text = "False", command = f11).grid(column = 2, row = 1)  
        q.mainloop()
        del questions[0]
        question +=1
    elif questions[0] == 'Question 12':
        print ("\n'The Raven' is the most famous poem by Edgar Allan Poe.")
        #choice = input(">>> ")
        def t12():
            global correct
            correct=correct+1
            print("\u001b[32mYou have answered correctly!\u001b[37m\n")
            q.destroy()
        def f12():
            #correct += 0
            print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
            q.destroy()
        q = tk.Tk()
        q.title("Python GUI App")  
        lbl = ttk.Label(q, text = "Enter the option:").grid(column = 0, row = 0)   
        b1 = ttk.Button(q, text = "True", command = t12).grid(column = 1, row = 1)  
        b2 = ttk.Button(q, text = "False", command = f12).grid(column = 2, row = 1)  
        q.mainloop()
        del questions[0]
        question +=1
    elif questions[0] == 'Question 13':
        print ("\nJeanne d'Arc gained command over the armies of France at the age of 19.")
        #choice = input(">>> ")
        def f13():
            global correct
            correct=correct+1
            print("\u001b[32mYou have answered correctly!\u001b[37m\n")
            q.destroy()
        def t13():
            #correct += 0
            print("\u001b[31mYour answer is incorrect.\u001b[37m\n")
            q.destroy()
        q = tk.Tk()
        q.title("Python GUI App")  
        lbl = ttk.Label(q, text = "Enter the option:").grid(column = 0, row = 0)   
        b1 = ttk.Button(q, text = "True", command = t13).grid(column = 1, row = 1)  
        b2 = ttk.Button(q, text = "False", command = f13).grid(column = 2, row = 1)  
        q.mainloop()
        del questions[0]
        question +=1

print ("\n\u001b[33mYou're finished, " + name.get() +". You got", correct, "out of 13 correct.\u001b[37m")

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
                    print("\u001b[31mSorry "+name.get()+", you lost! :< The secret word was:- \u001b[37m",secretWord)
                    print("\u001b[31mGame Over!\u001b[37m")

def print_word_to_guess(letters):
    #Utility function to print the current word to guess
    print("Word to guess: {0}".format(" ".join(guess_word)))

def print_guesses_taken(current, total):
    #Prints how many chances the player has used
    print("You are on guess {0}/{1}.\n".format(current, total))

change()
guessing()
