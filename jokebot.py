# Name:             Oto Drahonovsky
# Student Number:   10139126

# This file is provided to you as a starting point for the "jokebot.py" program of Assignment 2
# of CSP1150/CSP5110 in Semester 1, 2016.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.


# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter files run smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the required modules.
import tkinter
import tkinter.messagebox
import json


class ProgramGUI:

    def __init__(self):
        self.main = tkinter.Tk() #main window
        self.main.title('Joke Bot')        
        self.main.geometry("500x200")
        self.main.resizable(0,0)
        try:
            f = open("data.txt", "r")
            self.data = json.load(f)
            f.close()
        except:
            tkinter.messagebox.showerror("Error Message",
                                         "Missing/Invalid file")
            self.main.destroy()
            return
        self.currentJoke = 0
        self.setupLabel = tkinter.Label(self.main, font=("Verdana", 16), padx=10, pady=10)
        self.punchlineLabel = tkinter.Label(self.main, font=("Verdana", 16, "italic"), padx=10, pady=10)
        self.rateInfoLabel = tkinter.Label(self.main)
        self.ratingFrame = tkinter.Frame(self.main)
        
        self.ratingLabel = tkinter.Label(self.ratingFrame,
                                        text = "Your Rating: ")
        self.ratingEntry = tkinter.Entry(self.ratingFrame,
                                        width = 1)
        self.ratingButton = tkinter.Button(self.ratingFrame,
                                           text = "Submit",
                                           command = self.rateJoke)
        self.setupLabel.pack()
        self.punchlineLabel.pack()
        self.rateInfoLabel.pack()
        self.ratingLabel.pack(side = 'left')
        self.ratingEntry.pack(side = 'left')
        self.ratingButton.pack(side = 'left')
        self.ratingFrame.pack()

        self.showJoke()
        tkinter.mainloop()
        

        
        # This is the constructor of the class.
        # It is responsible for loading and reading the data file and creating the user interface.
        # See Points 1 to 4 "Requirements of jokebot.py" section of the assignment brief. 
        pass



    def showJoke(self):
        # This method is responsible for displaying a joke in the GUI.
        # See Point 1 of the "Methods in the GUI class of jokebot.py" section of the assignment brief.
        joke = self.data[self.currentJoke]
        self.setupLabel.configure(text = joke['setup'])
        self.punchlineLabel.configure(text = joke['punchline'])
        if joke['numOfRatings'] == 0:
            self.rateInfoLabel.configure(text = 'Joke has not been rated')
        else:
            self.rateInfoLabel.configure(
                text = "  Rated " + str(joke["numOfRatings"]) + " time(s). " + \
                "Average rating is " + str(round(joke["sumOfRatings"] / joke["numOfRatings"], 1)) + "/5."
                )
        self.ratingEntry.focus_set()
            



    def rateJoke(self):
        # This method is responsible for validating and recording the rating that a user gives a joke.
        # See Point 2 of the "Methods in the GUI class of jokebot.py" section of the assignment brief.
        joke = self.data[self.currentJoke]
        message = "Invalid rating.\n" \
                  "Enter an integer between 1 and 5."
        rating = self.ratingEntry.get()

        try:
            numRating = int(rating)
           
        except ValueError:
            tkinter.messagebox.showerror("Rating Error", message)
            return

        if numRating < 1 or numRating > 5:
            tkinter.messagebox.showerror("Rating Error", message)
            return
        else:
            joke['numOfRatings'] += 1
            joke['sumOfRatings'] += numRating
            f = open("data.txt", "w")
            json.dump(self.data, f)
            f.close()
            if len(self.data) - 1 == self.currentJoke:
                tkinter.messagebox.showinfo("Rating Recorded",
                                            "Thank you for rating.\n" \
                                            "That was the last joke.\n" \
                                            "The program will now end.")
                self.main.destroy()
            else:
                tkinter.messagebox.showinfo("Rating Recorded",
                                            "Thank you for rating.\n" \
                                            "The next joke will now appear.")
                self.currentJoke += 1
                self.ratingEntry.delete(0)
                self.showJoke()
                


# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()
