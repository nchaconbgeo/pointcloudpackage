import tkinter as tk
from tkinter import colorchooser

from classification import classification

class ClassificationPopup:
    """
    :description: Static class to manage classification popups. Data is written statically so it can be easily accessed after popup is finished. 
    :interracts with: Classification, ClassificationMenu
    """ 

    TEXT_WIDTH = 25
    DESCRIPTION_HEIGHT = 8
    WINDOW_NAME = "New Type"
    NAME_TEXT = "Name:"
    DESCRIPTION_TEXT = "Description:"
    COLOR_TEXT = "Choose Color"
    DONE_TEXT = "Done"
    
    defaultColor = "#ff00ff"
    nameField = None
    descriptionField = None
    colorButton = None
    chosenColor = defaultColor

    output = None
    frame = None

    def toClassification():
        """
        :description: Returns the inputted data to the popup as a Classification 
        :return: Classification of inputted data.
        :rtype: Classification.Classification
        """ 
        return Classification(name = ClassificationPopup.nameField.get(), description = ClassificationPopup.descriptionField.get("1.0", "end-1c"), color = ClassificationPopup.chosenColor)

    def pickColor():
        """
        :description: Open a popup window and save the result
        :return: None
        :rtype: None
        """ 

        Color = colorchooser.askcolor(title = ClassificationPopup.COLOR_TEXT)[1] #color code is the 2nd argument returned by the color chooser
        if Color != None: #cancelling yields a result of None
            ClassificationPopup.chosenColor = Color
            ClassificationPopup.colorButton.configure(bg = ClassificationPopup.chosenColor)

    def close():
        """
        :description: Close the frame and destroy all widgets within it
        :return: None
        :rtype: None
        """ 
        if ClassificationPopup.frame != None:
            ClassificationPopup.frame.destroy()
            ClassificationPopup.frame = None
            ClassificationPopup.chosenColor = ClassificationPopup.defaultColor

    def __init__(self, root, doneFunction):
        """
        :description: Create all the widgets for a  classification popup and display it to the user
        :return: The constructed class
        :rtype: ClassificationPopup
        """ 

        if ClassificationPopup.frame != None: #clear any old popups
            ClassificationPopup.frame.destroy()


        ClassificationPopup.frame = tk.Toplevel(root) # window
        ClassificationPopup.frame.title(ClassificationPopup.WINDOW_NAME)
      

        #labels and text fields
        ClassificationPopup.nameLabel = tk.Label(ClassificationPopup.frame, text = ClassificationPopup.NAME_TEXT)
        ClassificationPopup.nameField = tk.Entry(ClassificationPopup.frame, width = ClassificationPopup.TEXT_WIDTH)
        
        ClassificationPopup.descriptionLabel = tk.Label(ClassificationPopup.frame, text = ClassificationPopup.DESCRIPTION_TEXT)
        ClassificationPopup.descriptionField = tk.Text(ClassificationPopup.frame, width = ClassificationPopup.TEXT_WIDTH, height = ClassificationPopup.DESCRIPTION_HEIGHT, border = 2, relief = "groove")

        ClassificationPopup.colorButton = tk.Button(ClassificationPopup.frame, text = ClassificationPopup.COLOR_TEXT, bg = ClassificationPopup.chosenColor, command = ClassificationPopup.pickColor, pady = 15) #color picker button
        ClassificationPopup.doneButton = tk.Button(ClassificationPopup.frame, text = ClassificationPopup.DONE_TEXT, command = doneFunction, pady = 15) #done button

        #add to grid in descending order
        ClassificationPopup.nameLabel.grid(row = 0, sticky = 'W')
        ClassificationPopup.nameField.grid(row = 1, column = 0, sticky = 'EW')
                
        ClassificationPopup.descriptionLabel.grid(row = 2, column = 0, sticky = 'W')
        ClassificationPopup.descriptionField.grid(row = 3, column = 0, sticky = 'EW')
        
        ClassificationPopup.colorButton.grid(row = 4, column = 0, sticky = 'EW')
        ClassificationPopup.doneButton.grid(row = 5, column = 0, sticky = 'EW')

        ClassificationPopup.frame.grab_set() # grab focus
