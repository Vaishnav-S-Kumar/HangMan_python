import tkinter as tk
import random as r
import HMfigure as h

# Greetings
name=input("enter name:")
print(f"Hi {name}, Wlcome to HangMan Game")
print("-------Hang Man-------") 


# Wordlist
wordlist=["Hello","Python","Knight","Cybersecurity","Siberia"]
print(f"this is the list of words:\n{wordlist}")


# if c: --> checks if there is any input 
c=input("would you like to input a word['If yes, type word]:")
if c:
    if c in wordlist:
        print("word already in the list")
    else:                                            
        wordlist.append(c)
        print(f"this is the new list of words:\n{wordlist}")

# Word 
Word =r.choice(wordlist).lower()

# Hangman Figures
HM_Figures=[h.HM1,h.HM2,h.HM3,h.HM4,h.HM5,h.HM6]

# User input/Guess
guess=input("guess a Letter:").lower()
wrong=0
def guess_again():
    print("Oopsie, your guess was wrong")
    global guess 
    print(wordlist)
    guess = input("guess a Letter:").lower()

while wrong<6:
    if guess in Word:
        print("Yes")
        g_word=input("guess word:").lower()
        if g_word == Word:
            print("Yes, you have won")
        else:
            print("Sorry, you have failed")
            print(Word)
        break

    else:
        print("No")
        HM_Figures[wrong]()
        wrong+=1
        print(f"------- Guess {wrong+1}----------")
        guess_again()