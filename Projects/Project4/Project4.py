# AdventureGame
# Refs 
# https://www.makeuseof.com/python-text-adventure-game-create/
# https://reintech.io/blog/how-to-create-a-text-based-adventure-game-with-python
# https://www.google.com/search?q=loop+python+play+again&rlz=1C1CHBD_en-GBUS1021US1021&sxsrf=APwXEdfx5gZsX-9qcw2Zhls7xIdKqRDsHQ%3A1687027182593&ei=7v2NZMvuI-eA0PEPyeKUwAM&ved=0ahUKEwjLncf_-cr_AhVnADQIHUkxBTgQ4dUDCBA&uact=5&oq=loop+python+play+again&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIGCAAQFhAeMggIABCKBRCGAzIICAAQigUQhgMyCAgAEIoFEIYDMggIABCKBRCGAzoKCAAQRxDWBBCwAzoKCAAQigUQsAMQQzoHCCMQsQIQJzoGCAAQBxAeOgcIABCKBRBDOgUIABCABDoICAAQigUQkQI6CAgAEBYQHhAPOgUIIRCgAToICCEQFhAeEB1KBAhBGABQ_AFY7R1g6x9oAXABeACAAa4CiAHkEpIBCDAuMTMuMS4xmAEAoAEBwAEByAEK&sclient=gws-wiz-serp#fpstate=ive&vld=cid:7bfb550f,vid:O8ro4Gq1WMk
# My friend Morgan helped a lot with this assignment
# The story is my own, adpated from a screenplay and novel I am working on.

play = True
weapon = False

#The user chooses which direction to head and calls the function based on what they picked
def introScene():
  directions = ["left","right","forward","backward"]
  print("You are at a crossroads, deep in the canyon covered in a shroud of dark mist, which way will you go?")
  userInput = ""
  while userInput not in directions:
    print("Options: left/right/backward/forward")
    userInput = input()
    #If the user chooses left, the Wraith Creatue appears
    if userInput == "left":
      WraithCreature()
    #If the user chooses right, the user finds a cohearant soul
    elif userInput == "right":
      CohearantSoul()
    #If the user chooses forward, mist will appear
    elif userInput == "forward":
      DarkMist()
    #If they choose backward, they will then be prompted to picked another pathway since they must find the scythe.
    elif userInput == "backward":
      print("Don't forget, you must find the scythe at all cost, you cannot let L’appel du Vide (The Call of the Void) win.")
    #If the user does not input a valid option it will prompt them to do so.  
    else: 
      print("Please enter a valid option.")


#The user encounters an wraith-like enemy
def WraithCreature():
  directions = ["right","backward"]
  print("A strange creature, seemingly a tormented soul, making horrible shrieks appears in front of you and is slowly clawing its way toward you. You are terrified. Which way do you go?")
  #The user is prompted to choose a direction
  userInput = ""
  while userInput not in directions:
    print("Options: right/left/backward")
    #If the user chooses right, they go to the spider silk scene
    userInput = input()
    if userInput == "right":
      SpiderSilkScene()
    #If the user chooses left, they will be blocked by a hoard of weeping souls and must choose another direction.
    elif userInput == "left":
      print("You find this direction blocked with a hoard of weeping souls. You must press on " +name+ " , where will you go next?")
    #If the user chose backward, they go back to the introduction
    elif userInput == "backward":
      introScene()
    #If the user does not input a valid option it will prompt them to do so.  
    else:
      print("Please enter a valid option.")
#In this area the user encounters a strange spider-like silk
def SpiderSilkScene():
  directions = ["forward","backward"]
  print("You see a trail of faint spider-like webs made of a strange material. Where would you like to go next?")
  #The user is prompted to choose a direction
  userInput = ""
  while userInput not in directions:
    print("Options: forward/backward")
    userInput = input()
    #If they user chooses forward they will find the scythe
    if userInput == "forward":
      print("You find stairs that seem to be unnatural. You follow them down and see a hand reaching out of the ground holding the scythe. You grab the scythe from the hand and use its powers to escape the canyon quickly and return to Tafotila.")
      quit()
    #If the user chooses backward, they will encounter the Wraith
    elif userInput == "backward":
      WraithCreature()
    else:
      #If the user does not input a valid option it will prompt them to do so.  
      print("Please enter a valid option.")

#This area has a dark mist shrouding the area
def DarkMist():
  directions = ["right","left","backward"]
  print("You notice the mist gets darker and clouds your thoughts. Where would you like to go?")
  #The user is prompted to choose a direction
  userInput = ""
  while userInput not in directions:
    print("Options: right/left/backward")
    userInput = input()
    #If the user chooses right they will succumb to darkness and die
    if userInput == "right":
      print("The dark mist takes over your mind faster than you can retreat. You succomb to L’appel du Vide (The Call of the Void).")
      play_again = input ("Play again? (Y for yes N for no)".upper())
      if play_again == 'N':
        print("Thank you for you efforts, hero!")
        play = False 
        quit()
      elif play_again == 'Y':
        # This is the introduction to the game that the player sees
        if __name__ == "__main__":
          while True:
            print("You find yourself in a canyon in search of an ancient scythe said to bring death to those of a cruel nature and healing to those of good nature.")
            print("This scythe is crucial to your quest, you cannot return to yout friend, Tafotila, without it.")
            print("You can walk in different directions to search for the scythe.")
            print("What is your name, hero? ")
            name = input()
            print("Good luck, " +name+ ".")
            introScene()
    #If the user chooses left, they find the scythe
    elif userInput == "left":
      print("You find stairs that seem to be unnatural. You follow them down and see a hand reaching out of the ground holding the scythe. You grab the scythe from the hand and use its powers to escape the canyon quickly and return to Tafotila.")
      quit()
    #If the user chooses backward they return to the introduction
    elif userInput == "backward":
      introScene()
    else:
     #If the user does not input a valid option it will prompt them to do so.  
      print("Please enter a valid option.")

# This is an enemy that the player sees
def CohearantSoul():
  directions = ["backward","forward"]
  #The strange vial, said to be useful later in the user's journey
  global weapon
  print("You have been walking for a while and finally reach a crossroads. Where will you go now?")
  #The user is prompted to choose a direction
  userInput = ""
  while userInput not in directions:
    print("Options: left/backward/forward")
    #If the user chooses left, they find the weapon (vial)
    userInput = input()
    if userInput == "left":
      print("You find a soul, this one seems to be cohearant. It turns to look at you with sorrow. You walk closer. The soul whispers: I too once stood where you do " +name+ " Take this, I don't think you are ready for what lies ahead. The soul gives you a vial that can help you later on in your journey.")
      weapon = True
    #If the user chooses backward, they go to the introduction
    elif userInput == "backward":
      introScene()
    #If the user chooses forward, they meet Ally (my protagonist's foil character)
    elif userInput == "forward":
      Ally()
    #If the user does not input a valid option it will prompt them to do so.  
    else:
      print("Please enter a valid option.")
#This is where the user encounters Ally
def Ally():
  actions = ["fight","trust"]
  #The strange vial
  global weapon
  print("The mist gets thicker. You see a figure ahead and walk toward it. It looks like you, but different somehow... The figure begins telling you how much more wonderful things could be if you were like them. You start to believe them. You must choose, do you trust this version of yourself?")
  #The user is asked if they believe their shadow-self
  userInput = ""
  while userInput not in actions:
    print("Options: trust/fight")
    userInput = input()
    #If the user chooses fight and has the weapon value == true, they defeat their shadow self and find the scythe.
    if userInput == "fight":
      if weapon:
        print("You remember the vial the soul gave you and throw it at your shadowed reflection. It seems to dissapear with a pained laugh. After moving forward you find stairs that seem to be unnatural. You follow them down and see a hand reaching out of the ground holding the scythe.")
        print("You grab the scythe from the hand and use its powers to escape the canyon quickly and return to Tafotila.")
        quit()
      else:
      #If the user chooses fight and weapon does not equal true, they will succomb to the mist
        print("You thought you could fight off your shadowed self, but it was too late. The mist envelops you. You succomb to L’appel du Vide (The Call of the Void).")
        play_again = input ("Play again? (Y for yes, N for no)".upper())
      if play_again == 'N':
        print("Thank you for your efforts, " +name+ ".")
        play = False 
        quit()
      elif play_again == 'Y':
        #This is the introduction
        if __name__ == "__main__":
          while True:
            print("You find yourself in a canyon in search of an ancient scythe said to bring death to those of a cruel nature and healing to those of good nature.")
            print("This scythe is crucial to your quest, you cannot return to yout friend, Tafotila, without it.")
            print("You can walk in different directions to search for the scythe.")
            print("What is your name, hero? ")
            name = input()
            print("Good luck, " +name+ ".")
            introScene()
    #If the user chooses 
    elif userInput == "trust":
      print("Before the mist consumes you, a strange soul appears and takes you away.")
      CohearantSoul()
    else:
    #If the user does not input a valid option it will prompt them to do so. 
      print("Please enter a valid option.")
      


while play == True:
#This is the introduction that runs whenever play is true
  if __name__ == "__main__":
    while True:
      print("You find yourself in a canyon in search of an ancient scythe said to bring death to those of a cruel nature and healing to those of good nature.")
      print("This scythe is crucial to your quest, you cannot return to yout friend, Tafotila, without it.")
      print("You can walk in different directions to search for the scythe.")
      print("What is your name, hero? ")
      name = input()
      print("Good luck, " +name+ ".")
      introScene()