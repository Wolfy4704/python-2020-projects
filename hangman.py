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
WORDS = ("OVERUSED","CLAM","GUAM","COOKIE","PYTHON")
word = random.choice(WORDS)
#assignment
#10 python related word with one refering to the snake
#deffine the terms in comments
wrong = 0
used = []
so_far = "*"*len(word)

print("Welcome to Hangman. Good luck!")
print()
print(HANGMAN[wrong])
print(so_far)








##option1
##index = random.randint(0,len(WORDS)-1)
##word = WORDS[index]
##print(word)


##x = 0
##while x < len(HANGMAN):
##    print(HANGMAN[x])
##    input()
##    x+=1

















