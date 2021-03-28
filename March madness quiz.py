# Simple Quiz using Tkinter
  
#import everything from tkinter
from tkinter import *
  
# and import messagebox as mb from tkinter
from tkinter import messagebox as mb
  
#import json to use json file for data
import json
  
#class to define the components of the GUI
class Quiz:
    
    #Method sets Q's count to 0 and initializes counters and displays
    def __init__(self):
          
        # set question number to 0
        self.q_no=0
          
        # assigns questions to the display_question function to update later.
        self.display_title()
        self.display_question()
          
        # Holds integer for option
        self.opt_selected=IntVar()
          
        # displaying radio button and options for current question
        self.opts=self.radio_buttons()
          
        # display options for question
        self.display_options()
          
        # displays the button
        self.buttons()
          
        # number of questions
        self.data_size=len(question)
          
        # counter for correct
        self.correct=0
  
  
    # Used to display result and calculates correct and incorrect
    def display_result(self):
          
        # calculates the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
          
        # calcultaes the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
          
        # Shows box to display result
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")
  
  
    # check answer on click
    def check_ans(self, q_no):
          
        # check if correct
        if self.opt_selected.get() == answer[q_no]:
            # if option = correct, return true
            return True
  
    # Check answer if correct add 1 if not then continue.
    def next_btn(self):
          
        # Check if the answer is correct
        if self.check_ans(self.q_no):
              
            # if the answer is correct it increments the correct by 1
            self.correct += 1
          
        # Moves to next Question by incrementing the q_no counter
        self.q_no += 1
          
        # checks if the q_no size is equal to the data size
        if self.q_no==self.data_size:
              
            # if it is correct then it displays the score
            self.display_result()
              
            # destroys the GUI
            gui.destroy()
        else:
            # shows the next question
            self.display_question()
            self.display_options()
  
  
    # Shows buttons for next and quit and the placement for each
    def buttons(self):
          
        # The first button is the Next button to move to the
        # next Question
        next_button = Button(gui, text="Next",command=self.next_btn,
        width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
          
        # palcing the button  on the screen
        next_button.place(x=350,y=380)
          
        # This is the second button which is used to Quit the GUI
        quit_button = Button(gui, text="Quit", command=gui.destroy,
        width=5,bg="black", fg="white",font=("Times New Roman",16," bold"))
          
        # placing the Quit button on the screen
        quit_button.place(x=700,y=50)
  
  
    # Deselcts radio buttons and shows question options
    def display_options(self):
        val=0
          
        # deselecting the options
        self.opt_selected.set(0)
          
        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1
  
  
    # This method shows the current Question on the screen
    def display_question(self):
          
        # setting the Quetion properties
        q_no = Label(gui, text=question[self.q_no], width=60,
        font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
          
        #placing the option on the screen
        q_no.place(x=70, y=100)
  
  
    # This method is used to Display Title
    def display_title(self):
          
        # The title to be shown
        title = Label(gui, text="March Madness",
        width=50, bg="green",fg="white", font=("ariel", 20, "bold"))
          
        # place of the title
        title.place(x=0, y=2)
  
  
    #Shows question at specified point and radio buttons
    def radio_buttons(self):
          
        # initialize the list with an empty list of options
        q_list = []
          
        # position of the first option
        y_pos = 150
          
        # adding the options to the list
        while len(q_list) < 4:
              
            # setting the radio button properties
            radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
            value = len(q_list)+1,font = ("Times New Roman",14))
              
            # adding the button to the list
            q_list.append(radio_btn)
              
            # placing the button
            radio_btn.place(x = 100, y = y_pos)
              
            # incrementing the y-axis position by 40
            y_pos += 40
          
        # return the radio buttons
        return q_list
  
# Create a GUI Window
gui = Tk()
  
# set the size of the GUI Window
gui.geometry("850x450")
  
# set the title of the Window
gui.title("Erik's March Madness quiz")
  
# get the data from the json file
with open('data.json') as f:
    data = json.load(f)
  
# set the question, options, and answer
question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])
  
# create an object of the Quiz Class.
quiz = Quiz()
  
# Start the GUI
gui.mainloop()
  
# KIRE HATRED
#  #     #
# #      #
###
# #      #  #####   ######
#  #     #  #   #   #    #
#  #     #  #   #   ######
#   #    #  #       #
#    #   #  #       ######
