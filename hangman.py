#Brayden Woodard
#HangMan
#10/20

#imports
import random

HANGMAN = (
"""
----------
|    |
|     
|
|
|
|
--------------------------
""",
"""
----------
|    |
|    0
|
|
|
|
--------------------------
""",
"""
----------
|    |
|    0
|   -+-
|
|
|
--------------------------
""",
"""
----------
|    |
|    0
|   -+-\\
|
|
|
--------------------------
""",
"""
----------
|     |
|     0
|   /-+-\\
|
|
|
--------------------------
""",
"""
----------
|     |
|     0
|   /-+-\\
|      +
|    |
|    |
--------------------------
""",
"""
---------
|     |
|     0
|   /-+-\\
|      +
|    |  |
|    |  |
--------------------------
""")
MAX_WRONG = len(HANGMAN)-1
WORDS = ("CONSTRICTING","CLAM","GUAM","COOKIE","PYTHON")
word = random.choice(WORDS)
#assignment
#10 python related word with one refering to the snake
#deffine the terms in comments
#after the word is revealed show definition to user 
wrong = 0
used = []
so_far = "*"*len(word)

print("Welcome to Hangman. Good luck!")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nYouve used the following letters:\n",used)
    print("\nSo far the word is:\n",so_far)
    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()
    print(guess)


    while guess in used:
        print("youve already guessed that letter",guess)
        guess = input("Enter your guess: ")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print("\nYes!", guess, "is in the word!")

        #create new so_far to include guess in the correct location
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new+=guess
            else:
                new+=so_far[i]
        so_far = new

    else:
        print("\nSorry", guess, "isnt in the word.")
        wrong+=1


if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYouve been hanged!")
else:
    print("\nYou Guessed it!")

print("\nThe word was", word)

input("\n\nPress the enter key to exit")





