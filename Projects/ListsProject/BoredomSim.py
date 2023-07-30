#This project uses lists giving the user choices on what to do when they are bored or have one randly selected for them
#I learned how to do this by referencing my Rock, Paper, Scissors assignment and the code provided in the assignment.
#I used my favorit debugger, chatGPT as well, here is the link to my debugging conversation: https://chat.openai.com/share/a4101e31-07dc-41ac-be52-f4ae36278f6f

print("Welcome, it seems you're bored. The real dilemma is can you choose how to cure your boredom?")

#imports random functionality
import random

#setting up the inputs, options, and lists
UserInput = input("So, if I gave you a list would you pick? (Yes or No)")
PossibleActions = ["Yes", "No"]
BoredomCures = ["Read a book", "Watch a movie", "Watch a show", "Play a video game", "Read comics", "Clean"]
Indecisive = random.choice(BoredomCures)

#making a function for the user to pick an item from the list
def UserChoice():
    item_number = 0
    for each_item in BoredomCures:
        print(item_number, each_item)
        item_number = item_number + 1
    item_pick = int(input("Please enter the number of the boredom cure you would like: "))
    print("\nHere is what you have chosen: " + BoredomCures[item_pick])

#making a function to pick a random entry from the list
def RandomChoice():
    Indecisive = random.choice(BoredomCures)
    print("I will now choose something from the list at random")
    print(f"\nHere is your randomly chosen boredom cure: {Indecisive}")

#Choose the function based on the user input
if UserInput == "Yes":
    UserChoice()
elif UserInput == "No":
    RandomChoice()

#The goodbye
print("Have fun!")
