# Name:             Oto Drahonovsky
# Student Number:   10139126

# This file is provided to you as a starting point for the "admin.py" program of Assignment 2
# of CSP1150/CSP5110 in Semester 1, 2016.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.


# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter files run smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the json module to allow us to read and write data in JSON format.
import json



# This function repeatedly prompts for input until an integer is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
# CSP5110 Requirement: Also enforce a minimum value of 1.  See assignment brief.
def inputInt(prompt):
    while True:
        response = input(prompt)

        try:
            numResponse = int(response)
        except ValueError:
            continue
        else:
            if numResponse < 1:
                print("Enter value of at least 1!\n")
                continue
            else:
                return numResponse
            
            
            



# This function repeatedly prompts for input until something (not whitespace) is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def inputSomething(prompt):
    while True:
        response = input(prompt)
        if len(response.strip()) < 1:
            continue
        else:
            return str(response)


# This function opens "data.txt" in write mode and writes dataList to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def saveChanges(dataList):
    f = open("data.txt", "w")
    json.dump(dataList, f)
    f.close()




# Here is where you attempt to open data.txt and read the data / create an empty list if the file does not exist.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.
try:
    f = open("data.txt", "r")
    data = json.load(f)
    f.close()
except:
    data = []



# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Requirements of admin.py" section of the assignment brief.
# The rest is up to you.
print('Welcome to the Joke Bot Admin Program.')

while True:
    print('Choose [a]dd, [l]ist, [t]op, [s]earch, [v]iew, [d]elete or [q]uit.')
    choiceParts = input('> ').lower().split() # Prompt for input and convert it to lowercase.
        
    if choiceParts[0] == 'a':
        # Add a new joke.
        # See Point 3 of the "Requirements of admin.py" section of the assignment brief.
        setup = inputSomething("Enter setup of joke: ")
        punchline = inputSomething("Enter punchline of joke: ")
        newJoke = {"setup": setup,
                   "sumOfRatings": 0,
                   "punchline": punchline,
                   "numOfRatings": 0}
        data.append(newJoke)
        saveChanges(data)
        print("Joke added.\n")
        
    elif choiceParts[0] == 'l':
        if len(data) > 0:
            print("List of jokes:")
            # List the current jokes.
            # See Point 4 of the "Requirements of admin.py" section of the assignment brief.
            for i, joke in enumerate(data):
                print("  ", i + 1, ") ", joke["setup"], sep = "")
            print()
        else:
            print("There are no jokes saved.")
            
    elif choiceParts[0] == 't':
        if len(data) > 0:
            print("List of jokes that have an average rating of 4 or more:")
            # List the current jokes with rating of 4 or more.
            highRatedJokes = False
            for i, joke in enumerate(data):
                try:
                    rating = joke["sumOfRatings"] / joke["numOfRatings"]
                except ZeroDivisionError:
                    continue
                else:
                    if rating >= 4:
                        print("  ", i + 1, ") ", joke["setup"], sep = "")
                        highRatedJokes = True
            if not highRatedJokes:
                print("There are no jokes that have an average rating of 4 or more!")
            print()
        else:
            print("There are no jokes saved.")
            
    elif choiceParts[0] == 's':
        if len(data) > 0:
            if len(choiceParts) == 1:
                search = inputSomething("Enter search term: ").lower()
            else:
                search = ' '.join(choiceParts[1:])
            # Search the current jokes.
            # See Point 5 of the "Requirements of admin.py" section of the assignment brief.
            print("Search results:")
            noMatches = True
            for i, joke in enumerate(data):
                if search in joke["setup"].lower() or search in joke["punchline"].lower():
                    print("  ", i + 1, ") ", joke["setup"], sep = "")
                    noMatches = False
            if noMatches:
                print("No matches found.")
        else:
            print("There are no jokes saved.")
            
    elif choiceParts[0] == 'v':
        # View a joke.
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.
        if len(data) > 0:
            if len(choiceParts) == 1:
                jokeIndex = inputInt("Joke number to view: ") - 1
            else:
                jokeIndex = int(choiceParts[1]) - 1
            try:
                print("\n  ", data[jokeIndex]["setup"], "\n  ",
                    data[jokeIndex]["punchline"], "\n", sep = "")
                if data[jokeIndex]["numOfRatings"] == 0:
                    print("  This joke has not been rated.\n")
                else:
                    print("  Rated ", data[jokeIndex]["numOfRatings"], " time(s). " + \
                            "Average rating is ",
                            round(data[jokeIndex]["sumOfRatings"] / data[jokeIndex]["numOfRatings"], 1),
                            ".", sep = "")
            except IndexError:
                print("Invalid index number.")
                
        else:
            print("There are no jokes saved.")
            
    elif choiceParts[0] == 'd':
        # Delete a joke.
        # See Point 7 of the "Requirements of admin.py" section of the assignment brief.
        if len(data) > 0:
            if len(choiceParts) == 1:
                jokeIndex = inputInt("Joke number to delete: ") - 1
            else:
                jokeIndex = int(choiceParts[1]) - 1
            try:
                del data[jokeIndex]
                saveChanges(data)
                print("Joke deleted.")
            except IndexError:
                print("Invalid index number.")
        else:
            print("There are no jokes saved.")
            
    elif choiceParts[0] == 'q':
        # Quit the program.
        # See Point 8 of the "Requirements of admin.py" section of the assignment brief.
        print("Goodbye!")
        break
    
    else:
        # Print "invalid choice" message.
        # See Point 9 of the "Requirements of admin.py" section of the assignment brief.
        print("Invalid choice!")
