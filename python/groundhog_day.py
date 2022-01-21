import sys
import time

timeDelay = 2
readSpeed = 0.2
slowReadSpeed = 0.08
displaySpeed = 0.03

correctAnswer = False

ding = "Ding!     Time rewinds a bit..."
ding2 = "DING!"
ding3 = """
DDD    I  N   N   GGGG   !!
D  D   I  NN  N  G       !!
D   D  I  N N N  G  GG   !!
D  D   I  N  NN  G    G  !!
DDD    I  N   N   GGGG   oo
"""

def display(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)
  time.sleep(2)

title = """******************
* The Blind date *
******************"""
print()
print()
print()
print(title)
print()
print()
print()
time.sleep(2)

tries = 1
gameover = False

text1 = """You have been set up on a blind date by your good friend Sally.
You are on a long streak of bad dates and are hoping that this could be
the one to end it."""
text2 = """\"Maybe they could be the one?\" you say to yourself
as you reach the restaurant that you chose."""
choice1 = """Which restaruant did you choose?
    #1 McDonald\'s
    #2 Le Chateaux"""

display(text1)
print()
while correctAnswer == False:
  display(text2)
  print()
  display(choice1)
  print()
  choice1_1 = input("Type number then hit ENTER (1/2): ")
  if choice1_1 == '1':
    print()
    time.sleep(1)
    print(ding)
    time.sleep(1)
  elif choice1_1 == '2':
    display(title)
    correctAnswer = True
  print()


