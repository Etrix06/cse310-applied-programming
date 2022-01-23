import sys
import time

##Classes##
class Date:
  def __init__(self, name, sex, dateName):
      self.name = name
      self.sex = sex
      self.dateName = dateName



##Functions##
def endgameCheck(gameover, tries):
  if gameover == True and tries <= 3:
    return True
  else:
    return False

def display(text):            #displays text slowly with delay at end
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)
  time.sleep(2)

def q_display(text):            #displays text quicker with no delay end
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.02)
  
#### Title Text ####
title = """********************************
* The Groundhog Day Blind date *
********************************"""
title2 = "A time-loop text adventure."

#### Dings ####
ding = ("Ding     Time rewinds a bit...  Giving you another chance", "DING!      Time yanks you back harshly...   yet another chance to fix your mistake.", """
DDD    I  N   N   GGGG   !!
D  D   I  NN  N  G       !!
D   D  I  N N N  G  GG   !!
D  D   I  N  NN  G    G  !!
DDD    I  N   N   GGGG   oo

You are running out of chances...
""", """\n\n\nYou ran out of chances, the sad date ended and you are doomed
to a sad, lonely life.""")

### Story Text lines ###
                        ##First loop##
text1 = """\n\n\nYou have been set up on a blind date by your good friend Sally.
You are on a long streak of bad dates and are hoping that this could be
the one to end it."""
text2 = """\"Maybe they could be the one?\" You say to yourself
as you reach the restaurant that you chose."""
                        ##Second loop##
text3 = "\"Welcome to Le Chateau\" says the hostess as a greeting.  \"How many in your party?\""

text4 = "\n\"Your table is Ready, right this way.\" The hostess says.\n"

                        ##3rd loop##
text5 = """\nAs you are being led to the table you turn around to see your date arrive.
You awkwardly wave at them, and they come over to greet you.\n"""
text6 = "\"Hi\" you say nervously. \"I\'m"

                        ##4th loop##
text7_2 = "\"Sally said you were good looking but Dang.\"\n"
text7 = "\"Yes, it's great to finally meet you, Sally talks about you often.\" You say.\n"

text8 = """\"Good things mostly, I think she has been trying to
hook us up for a while.\" You say.\n"""

text8_2 = "\"She can be sort of annoying sometimes.\"\n"

text9 = "\"Yes, she has talked to me about you as well.\" "

text10 = """\n\"Good things I hope.\" You say as they smile an nod. 
\"Shall we sit down?\" You say.\n"""

text11 = """You make an awkward attempt to pull the chair out for her.  She
smiles and lets you be chivalrous.
\"Thank you.\" She says.
\"Your waiter will be right with you.\" Says the hostess.\n"""

text12 = """You begin to pull out your chair when he makes an awkward
attempt to pull out your chair.  You smile and let him be chivalrous.
\"Thank You.\" You say.
\"Your waiter will be right with you.\" Says the hostess.\n"""

text13 = """\nAfter a few moments your waitress shows up to give you
the menu and to take your drink order.\n"""

text14 = "\"This is really a fancy place.\" "

text15 = "\"I know, I was unsure of it, but I heard the food is good.\"\n"

text16 = "\"I\'ve heard that too.\" "

text17 = "\"If you ask me, you can't go wrong with McDonalds fries.\" You say.\n"

text18 = "\"Is it wrong that I just want a hamburger?.\" You say.\n"

    ##5th loop
text19 = "\"I know! I love McDonalds.\" "

text20 = "\nThe waitress shows back up, \"Are you guys ready to order?\" She says.\n"

text21 = "\n\nAnd for the first time this night you though to yourself, \n" 
text22 = "\"This might actually turn into a good date.\"\n"
text23 = "You went on to have a lovely date.\n"

### Questions and Choices ###
choice1 = """\nWhich restaruant did you choose?
    #1 McDonald\'s
    #2 Le Chateau"""

choice2 = """\nChoose one?
    #1 \"Just me.\"
    #2 \"Two Please\"
    #3 \"I called a reservation for a table\""""

choice3 = """\n
***What do you say next?
    #1 \"Sally said you were good looking but Dang.\"
    #2 \"Yes, it's great to finally meet you, Sally talks about you often.\""""

choice4 = """\n
***What do you say next?
    #1 \"Good things mostly, I think she has been trying to
         hook us up for a while.\"
    #2 \"She can be sort of annoying sometimes.\""""

choice5 = """\n
***What do you say next?
    #1 \"I know, I bring all my dates here.\"
    #2 \"I know, I was unsure of it, but I heard the food is good.\""""

choice6 = """\n
***What do you say next?
    #1 \"If you ask me, you can't go wrong with McDonalds fries.\"
    #2 \"Is it wrong that I just want a hamburger?.\""""
