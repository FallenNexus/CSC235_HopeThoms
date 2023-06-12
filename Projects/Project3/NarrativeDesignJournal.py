#this will be the narrative design hournal for the file I/O assignment
#This will be able to acess past entries

#import time extension
#this will allow date and time integration

#create an intro for the user
import datetime


print("\n\n\t *** Welcome to your narrative design journal ***\n\n")
print("This program will allow you to write and view past design entires")
print("Would you like to view past entries or write a new one?")

#ask the user if they want to write a new entry or view an old one
#this variable will store the user's choice
user_choice = input("Enter 'view' to view a past entry or 'new' to record a new entry: ")

#verify the user choice
#based on what they input changes the code that gets executed

#if the user enters "new" the program will execute this code
if user_choice == "new":
    
    entry = input("Type in your new entry. Press Enter when finished. ")

    #get current date and time to stamp the entry
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #Open file in append mode. Append mode will add the new entry to the end of the file
    #creates new file if it does not exist

    with open("NDjournal.txt", "a") as journal:
        #write the date, time, and entry to the file
        journal.write(f"(now): {entry}\n")

    #print out confirmation
    print("Your Narrative Design Journal Entry has been recorded.\n\n")

#if the user enters "view" the program execute this code
#this means the program reads the files instead of writing to them

elif user_choice == "view":
    #open the NDjournal.txt in read mode. Starting with try block. This handles errors if the file doesnt exist
    try:
        with open("NDjournal.txt", "r") as journal:
            #read the contents of the file and store it in the contents variable
            entries = journal.readlines()

            #If no entries are found
            if not entries:
                print("No entries were found, create a new story first")

            #if entries are found, print them
            else:
                print("Summoning your past creativity, hang tight while it loads.")
                
                #loops through each entry
                for entry in entries:
                    print(entry)
    #if the file doesn't exist, print error message
    except FileNotFoundError:
        print("No entries found, create a new story first")

#if the user input is invalis, this code will run
else:
    print("\n\n !!! Oh no, it seems like you chose the wrong narrative. Please enter 'new' or 'view'.\n\n")
    