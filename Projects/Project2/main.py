#I used my old Rock, Paper, Scissors program for this
#I got this theme idea from: https://wrpsa.com/different-variations-of-rock-paper-scissors/

print("Let's play Hobbit, Elf, Orc!")
print("The rules are simple,")
print("Hobbit beats Elf.")
print("Elf beats Orc.")
print("Orc beats Hobbit.")

#Fuction that can be called to loop everything easier
def RockPaperScissorsFunction():
    print("Let's play Hobbit, Elf, Orc!")

    #imports the random functionality (package)
    import random

    #Adds user input while also printing text
    user_action = input("Type your move (Hobbit, Elf, Orc): ")

    #variable of possible actions for the player and computer to choose from
    possible_actions = ["Hobbit", "Elf", "Orc"]

    #variable to call that allows the computer to choose rock, paper, or scissors randomly
    computer_action = random.choice(possible_actions)
    
    #Prints the pre-programmed text, stored user_action, and computer_action
    print(f"\nYou chose {user_action}, The computer chose {computer_action}.\n")
    
    #if the user action and computer action are the same it prints a tie
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    
     #If the user picks Hobbit it prints the corresponding text based upon what the random chose
    elif user_action == "Hobbit":
        if computer_action == "Elf":
            print("Hobbit destroys Elf! You win!")
        else:
            print("Orc kills Hobbit! You lose.")

    #If the user picks Elf it prints the corresponding text based upon what the random chose
    elif user_action == "Elf": 
        if computer_action == "Orc":
            print("Elf shoots Orc! You win!")
        else:
            print("Hobbit gets second breakfast! You lose.")
    
    #If the user picks Orc it prints the corresponding text based upon what the random chose
    elif user_action == "Orc": 
        if computer_action == "Hobbit":
            print("Orc brutally murders Hobbit! You win!")
        else:
            print("Elf chops your arm off! You lose.") 

#Loops the entire fuction
while True:
    RockPaperScissorsFunction()