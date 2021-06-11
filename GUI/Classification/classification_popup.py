import tkinter as tk
from tkinter import colorchooser
import random
from GUI.Classification import classification

class ClassificationPopup:
    """
    :Description: Static class to manage classification popups. Data is written statically so it can be easily accessed after popup is finished. 
    :interracts with: Classification, ClassificationMenu
    """ 

    TEXT_WIDTH = 25
    DESCRIPTION_HEIGHT = 8

    WINDOW_NAME_NEW = "New Type"
    WINDOW_NAME_CHANGE = "Edit Type"


    NAME_TEXT = "Name:"
    DESCRIPTION_TEXT = "Description:"
    COLOR_TEXT = "Choose Color"
    DONE_TEXT = "Done"
    
    defaultColor = "#ffffff"
    nameField = None
    descriptionField = None
    colorButton = None
    chosenColor = defaultColor

    output = None
    frame = None

    def toClassification():
        """
        :Description: Returns the inputted data to the popup as a Classification 
        """ 
        return classification.Classification(name = ClassificationPopup.nameField.get(), description = ClassificationPopup.descriptionField.get("1.0", "end-1c"), color = ClassificationPopup.chosenColor)

    def pickColor():
        """
        :Description: Open a popup window and save the result
        """ 

        color = colorchooser.askcolor(title = ClassificationPopup.COLOR_TEXT)[1] #color code is the 2nd argument returned by the color chooser
        if color != None: #cancelling yields a result of None
            ClassificationPopup.chosenColor = color
            ClassificationPopup.colorButton.configure(bg = ClassificationPopup.chosenColor)

    def close():
        """
        :Description: Close the frame and destroy all widgets within it
        """ 
        if ClassificationPopup.frame != None:
            ClassificationPopup.frame.destroy()
            ClassificationPopup.frame = None

    def __init__(self, root, doneFunction, currentClassification = None ):
        """
        :Description: Create all the widgets for a  classification popup and display it to the user
        :return: classification_popup
        """ 
        if ClassificationPopup.frame != None: #clear any old popups
            ClassificationPopup.frame.destroy()

        ClassificationPopup.frame = tk.Toplevel(root) # window

        #if we don't specify a color we assign it a randomized color
        self.chosenColor = "#"
        for i in range(6):
            index = random.randint(0, 11)
            self.chosenColor = self.chosenColor + ('4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')[index]



        if(currentClassification == None):
            ClassificationPopup.frame.title(ClassificationPopup.WINDOW_NAME_NEW)
        else:
            ClassificationPopup.frame.title(ClassificationPopup.WINDOW_NAME_CHANGE)
      
        #labels and text fields
        ClassificationPopup.nameLabel = tk.Label(ClassificationPopup.frame, text = ClassificationPopup.NAME_TEXT)
        ClassificationPopup.nameField = tk.Entry(ClassificationPopup.frame, width = ClassificationPopup.TEXT_WIDTH)
        
        ClassificationPopup.descriptionLabel = tk.Label(ClassificationPopup.frame, text = ClassificationPopup.DESCRIPTION_TEXT)
        ClassificationPopup.descriptionField = tk.Text(ClassificationPopup.frame, width = ClassificationPopup.TEXT_WIDTH, height = ClassificationPopup.DESCRIPTION_HEIGHT, border = 2, relief = "groove")

        ClassificationPopup.colorButton = tk.Button(ClassificationPopup.frame, text = ClassificationPopup.COLOR_TEXT, bg= ClassificationPopup.chosenColor, highlightbackground= ClassificationPopup.chosenColor, command = ClassificationPopup.pickColor, pady = 15) #color picker button
        ClassificationPopup.doneButton = tk.Button(ClassificationPopup.frame, text = ClassificationPopup.DONE_TEXT, command = doneFunction, pady = 15) #done button

        #add to grid in descending order
        ClassificationPopup.nameLabel.grid(row = 0, sticky = 'W')
        ClassificationPopup.nameField.grid(row = 1, column = 0, sticky = 'EW')
                
        ClassificationPopup.descriptionLabel.grid(row = 2, column = 0, sticky = 'W')
        ClassificationPopup.descriptionField.grid(row = 3, column = 0, sticky = 'EW')
        
        ClassificationPopup.colorButton.grid(row = 4, column = 0, sticky = 'EW')
        ClassificationPopup.doneButton.grid(row = 5, column = 0, sticky = 'EW')

        if(currentClassification != None):
            ClassificationPopup.nameField.insert(0, currentClassification.name)
            ClassificationPopup.descriptionField.insert('insert', currentClassification.description)
            ClassificationPopup.chosenColor = currentClassification.color
            ClassificationPopup.colorButton.configure(bg=ClassificationPopup.chosenColor, highlightbackground= ClassificationPopup.chosenColor)
            if (currentClassification.classificationID == 0): 
                ClassificationPopup.colorButton.configure(state = 'disabled')
            
                

        ClassificationPopup.frame.grab_set() # grab focus
