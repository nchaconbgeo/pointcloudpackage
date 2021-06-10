import application
import tkinter as tk

import GUI.Classification.classification_popup as classificationPopup
import GUI.Classification.classification as classification

#library for making partial functions
from functools import partial


class ClassificationMenu:
    WINDOW_NAME = "Point Classifications"
    ADD_TEXT = "New Classification"
    BUTTON_WIDTH = 16

    classificationButtons = []
    newClassificationButton = None

    buttonFrame = None

    frame = None
    root = None
    app = None

    def doneAddingClassification(self):
        """
        :description: callback from the done button, which copies data from the popup and adds it to the list
        """ 

        self.app.pointData.classifications.append(classificationPopup.ClassificationPopup.toClassification())
        
        classificationPopup.ClassificationPopup.close()
        self.rebuildButtons()

    def doneModifyingClassification(self, index):
        """
        :description: callback from the done button, which copies data from the popup into the element at index
        :param index: (int) index of classification to modify
        """ 
        self.app.pointData.classifications[index] = classificationPopup.ClassificationPopup.toClassification()
        classificationPopup.ClassificationPopup.close()
        self.rebuildButtons()

    def rebuildButtons(self):
        """
        :description: removes up all the old buttons for classification editing and finishing as well as re-adds them in the correct order
        """ 
        for button in self.classificationButtons:
            button.destroy()

        i = 0 #index of current button

        for classification in self.app.pointData.classifications:
            button = tk.Button(self.frame, text = classification.name, highlightbackground = classification.color, width = self.BUTTON_WIDTH, height = 0, command = partial(self.editButton, i), pady=5)
            button.grid(row = i + 1, column = 0, padx = 5) #0th slot taken up by label
            self.classificationButtons.append(button)
            i += 1
        
        if self.newClassificationButton != None:
            self.newClassificationButton.destroy()    

        self.newClassificationButton = tk.Button(self.frame, text = ClassificationMenu.ADD_TEXT, command = self.newClassification) 
        self.newClassificationButton.grid(row = i + 1, column = 0) #preceding slots taken up by classifications and label


    def editButton(self, index):
        """
        :description: launch the popup for editing a classification
        :param index: (int) index of classification to modify
        """ 
        classificationPopup.ClassificationPopup(self.root, partial(self.doneModifyingClassification, index), currentClassification=self.app.pointData.classifications[index])

    def newClassification(self):
        """
        :description: launch the popup for creating a new classification
        """ 
        classificationPopup.ClassificationPopup(self.root, self.doneAddingClassification)

    def modifyClassification(self, index):
        """
        :description: launch the popup for editing a classification
        """ 
        classificationPopup.ClassificationPopup(self.root, self.done)
            

    def runCloseFunction(self):
        """
        :description: run the callback function if the user exits out of the window, if it's been set
        """ 
        self.frame.destroy()
        if(self.closeFunction != None):
            self.closeFunction()

    def __init__(self, root, app, closeFunction = None):
        """
        :description: Create the menu object that shows classifications
        :param root: (tkinter.Tk) the root context to create the window in
        :param app: (application) the application, which holds the pointData
        :param closeFunction: (function) a function to run when the window exit is clicked.
        """ 
        self.closeFunction = closeFunction
        self.root = root
        self.app = app
        
        self.frame = tk.Toplevel(root)
        self.frame.title(ClassificationMenu.WINDOW_NAME)

        if(closeFunction != None):
            self.closeFunction = closeFunction
            self.frame.protocol("WM_DELETE_WINDOW", self.runCloseFunction)

        label = tk.Label(self.frame, text = ClassificationMenu.WINDOW_NAME)
        label.grid(row = 0, column = 0)

        self.rebuildButtons()

