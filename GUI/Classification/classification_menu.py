import tkinter as tk

from classification_popup import ClassificationPopup
import classification

#library for making partial functions
from functools import partial


class ClassificationMenu:
    WINDOW_NAME = "Point Classifications"
    ADD_TEXT = "New Classification"

    classificationButtons = []
    newClassificationButton = None

    buttonFrame = None

    frame = None
    root = None
    def doneAddingClassification(self):
        Classification.classifications.append(ClassificationPopup.toClassification())

        
        ClassificationPopup.close()
        self.rebuildButtons()

    def doneModifyingClassification(self):
        result = ClassificationPopup.toClassification()
        
        ClassificationPopup.close()
        self.rebuildButtons()

    def rebuildButtons(self):

        for button in self.classificationButtons:
            button.destroy()
        i = 0
        for classification in Classification.classifications:
            button = tk.Button(self.frame, text = classification.name, bg = classification.color, width = 8, height = 0, command = partial(self.printButtonInfo, i))
            button.grid(row = i + 1, column = 0, padx = 5) #0th slot taken up by label
            self.classificationButtons.append(button)
            i += 1
        
        if self.newClassificationButton != None:
            self.newClassificationButton.destroy()    

        self.newClassificationButton = tk.Button(self.frame, text = ClassificationMenu.ADD_TEXT, command = self.newClassification) 
        self.newClassificationButton.grid(row = i + 1, column = 0) #preceding slots taken up by classifications and label


    def printButtonInfo(self, index):
        print(Classification.classifications[index].name)

    def newClassification(self):
        ClassificationPopup(self.root, self.doneAddingClassification)

    def modifyClassification(self, index):
        ClassificationPopup(self.root, self.done)
            

    def runCloseFunction(self):
        self.frame.destroy()
        if(self.closeFunction != None):
            self.closeFunction()

    def __init__(self, root, closeFunction = None):
        self.closeFunction = closeFunction
        self.root = root
        
        self.frame = tk.Toplevel(root)
        self.frame.title(ClassificationMenu.WINDOW_NAME)

        if(closeFunction != None):
            self.closeFunction = closeFunction
            self.frame.protocol("WM_DELETE_WINDOW", self.runCloseFunction)

        label = tk.Label(self.frame, text = ClassificationMenu.WINDOW_NAME)
        label.grid(row = 0, column = 0)

        self.rebuildButtons()