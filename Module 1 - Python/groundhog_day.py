import time
import gdfunctions as gd

### Variables ###
correctAnswer = False     #used in while loops
tries = 0                 #keeps track of wrong answers. 4 wrong is the end.
gameover = False

### Title ###
print()
print()
print()
print(gd.title)
time.sleep(1)
gd.display(gd.title2)
print()
print()
time.sleep(2)

question = """Before you begin,
What is your sex?
      #1 Male 
      #2 Female\n""" 
gd.q_display(question)
sex = input("Please select 1 or 2 and ENTER: ")

gd.display(gd.text1)
print()
while gameover == False:    #Game Loop

  ### First time Back loop ###
  while correctAnswer == False:
    gd.display(gd.text2)
    print()
    gd.q_display(gd.choice1)
    print()
    choice1_1 = input("Type number then hit ENTER (1/2): ")
    if choice1_1 == '1':       #wrong choice
      print()
      time.sleep(1)
      print(gd.ding[tries])
      tries = tries + 1
      time.sleep(1)
      if tries > 3:            #You get 3 tries on fourth it breaks and game over
        gameover = True            
        break
    elif choice1_1 == '2':     #right choice
      correctAnswer = True
      break
    else:
      gd.q_display("\nPlease enter one of the choices.\n")
    print()

  #end game check
  if gameover == True:
    break
  endgame = gd.endgameCheck(gameover, tries)
  if endgame == True:
    gameover = True
    break
    

  ### 2nd time Back loop ###
  correctAnswer = False      #variable resets to false

  while correctAnswer == False:
    print()
    gd.display(gd.text3)   #welcome to Le...
    gd.q_display(gd.choice2)
    print()
    choice2_1 = input("Type number then hit ENTER (1/2/3): ")
    if choice2_1 == '1':     #Wrong
      print()
      time.sleep(1)
      print(gd.ding[tries])
      tries = tries + 1
      time.sleep(1)
      if tries > 3:            #You get 3 tries on fourth it breaks and game over
        gameover = True            
        break
    elif choice2_1 == '2':    #Wrong
      gd.display("\n\"There is going to be an hour wait.\" The hostess says.\n")
      time.sleep(1)
      print(gd.ding[tries])
      tries = tries + 1
      time.sleep(1)
      if tries > 3:            #You get 3 tries on fourth it breaks and game over
        gameover = True            
        break
    elif choice2_1 == '3':   #Correct
      name = input("\nWhat is your name?\n")
#       sex = input("""
# What is your sex?
#       #1 Male 
#       #2 Female  
# Please select 1 or 2 and ENTER: """)
      dateName = input("\nWhat is your date's name?\n")
      date = gd.Date(name, sex, dateName)           #create a date object
      tempText = "\"Welcome, " + date.name +".\""
      gd.display(tempText)
      gd.display(gd.text4)   #Your table is ready ...
      correctAnswer = True
      break
    else:
      gd.q_display("\nPlease enter one of the choices.\n")
    print()

  #end game check
  if gameover == True:
    break
  endgame = gd.endgameCheck(gameover, tries)
  if endgame == True:
    gameover = True
    break
  
  ### 3nd time Back loop ###
  correctAnswer = False      #variable resets to false
  
  #remove
  #date = gd.Date("Erik", 1, "Griscel")  #remove this
  
  gd.display(gd.text5)
  gd.q_display(gd.text6)
  gd.display(" " + date.name + ".\n")
  
  
  while correctAnswer == False:
    tempText = "\"I\'m " + date.dateName + ", good to meet you.\" "
    gd.q_display(tempText)
    #print(gd.date.sex)
    if date.sex == '1':
       tempText = "She says."
       gd.display(tempText)
    elif date.sex == '2':
      tempText = "He says."
      gd.display(tempText)
    gd.q_display(gd.choice3)
    response = input("\nPlease choose 1 or 2 and ENTER:\n")
    if response == '1':       #wrong choice  You're pretty
      print()
      gd.display(gd.text7_2)
      time.sleep(1)
      print(gd.ding[tries])
      tries = tries + 1
      time.sleep(1)
      if tries > 3:            #You get 3 tries on fourth it breaks and game over
        gameover = True            
        break
    elif response == '2':     #right choice  sally talks about you.
      gd.display(gd.text7)
      correctAnswer = True
      break
    else:
      gd.q_display("\nPlease enter one of the choices.\n")
    print()

  #end game check
  if gameover == True:
    break
  endgame = gd.endgameCheck(gameover, tries)
  if endgame == True:
    gameover = True
    break

  ### 4th time Back loop ###
  correctAnswer = False      #variable resets to false
  
  while correctAnswer == False:
    tempText = "\"Really, what does she say about me?\" "
    gd.q_display(tempText)
    if date.sex == '1':
       tempText = "She says."
       gd.display(tempText)
    elif date.sex == '2':
      tempText = "He says."
      gd.display(tempText)

    #gd.display(gd.text7)
    gd.q_display(gd.choice4)
    response = input("\nPlease choose 1 or 2 and ENTER:\n")
    if response == '1':       #right choice   good things
      gd.display(gd.text8)
      correctAnswer = True
      break
    elif response == '2':     #wrong choice   shes annoying
      print()
      gd.q_display(gd.text8_2)
      time.sleep(1)
      print(gd.ding[tries])
      tries = tries + 1
      time.sleep(1)
      if tries > 3:            #You get 3 tries on fourth it breaks and game over
        gameover = True            
        break
    else:
      gd.q_display("\nPlease enter one of the choices.\n")
  #end game check
  if gameover == True:
    break
  endgame = gd.endgameCheck(gameover, tries)
  if endgame == True:
    gameover = True
    break
  gd.q_display(gd.text9)   #she has talked to me too.
  if date.sex == '1':
      tempText = "She says."
      gd.display(tempText)
  elif date.sex == '2':
    tempText = "He says."
    gd.display(tempText)
  gd.display(gd.text10)    #good things i hope.  lets sit
  if date.sex == '1':
    gd.display(gd.text11)  #male response
  elif date.sex == '2':
    gd.display(gd.text12)  #female response
### 4th time back loop
  correctAnswer = False
  while correctAnswer == False:  
    gd.display(gd.text13)
    gd.q_display(gd.text14)
    tempText = date.dateName + " says.\n"
    # if date.sex == '1':
    #   tempText = "She says."
    #   gd.display(tempText)
    # elif date.sex == '2':
    #   tempText = "He says."
    gd.display(tempText)
    gd.q_display(gd.choice5)
    response = input("\nPlease choose 1 or 2 and ENTER:\n")
    if response == '1':       #wrong choice  You're pretty
      print()
      time.sleep(1)
      print(gd.ding[tries])
      tries = tries + 1
      time.sleep(1)
      if tries > 3:            #You get 3 tries on fourth it breaks and game over
        gameover = True            
        break
    elif response == '2':     #right choice  sally talks about you.
      gd.display(gd.text15)
      correctAnswer = True
      break
    else:
      gd.q_display("\nPlease enter one of the choices.\n")
  #end game check
  if gameover == True:
    break
  endgame = gd.endgameCheck(gameover, tries)
  if endgame == True:
    gameover = True
    break    
  gd.q_display(gd.text16)
  if date.sex == '1':
      tempText = "She says."
      gd.display(tempText)
  elif date.sex == '2':
    tempText = "He says."
    gd.display(tempText)
  gd.q_display(gd.choice6)
  response = input("\nPlease choose 1 or 2 and ENTER:\n")
  if response == '1':
    gd.display(gd.text17)
    
  elif response == '2':
    gd.display(gd.text18)
    
  
  ### 5th time back loop

  gd.q_display(gd.text19)
  if date.sex == '1':
    tempText = "She says.\n"
    gd.display(tempText)
  elif date.sex == '2':
    tempText = "He says.\n"
    gd.display(tempText)    
  gd.display(gd.text20)
  gd.display(gd.text21)
  gd.display(gd.text22)
  gd.display(gd.text23)
  gameover = True
  #end game check
  if gameover == True:
    break
  endgame = gd.endgameCheck(gameover, tries)
  if endgame == True:
    gameover = True
    break
### End of Game ###
if tries < 3 and gameover == True: 
  print("\n\nYou had a great date!  Thanks for playing!\n\n\n")
else:

  print("\n\nGAME OVER...The End\n\n\n\n")


