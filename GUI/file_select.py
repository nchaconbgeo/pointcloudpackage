import tkinter as tk
from tkinter import filedialog

class FileSelect:
    
    frame = None
    selectedFile = ""
    selectionButton = None

    selectedLabel = None
    fileLabel = None

    closeFunction = None

    BUTTON_TEXT = "Select File"
    WINDOW_NAME = "Import File"
    SELECTED_TEXT = "Selected File:"
    INITIAL_FILE_TEXT = "None"
    DONE_TEXT = "Done"


    def select_file(self):
        """
        :description: prompt the user to select a file from their filesystem
        :return: None
        """ 
        filetypes = (
            ("text files", "*.txt"),
            ("pcd files", "*.pcd"),
            ("ply files", "*.ply"),
            ("All files", "*.*")
            )

        selectedFile = filedialog.askopenfilename(
            title="Open a file",
            initialdir=".",
            filetypes=filetypes)

        if(selectedFile == None or selectedFile == ()):
            return #user cancelled selection operation

        self.selectedFile = selectedFile
        self.fileLabel.config(text = self.selectedFile)
        self.doneButton.config(state = "normal")

    def runCloseFunction(self):
        """
        :description: run the specified callback function when the window is closed
        :return: None
        """ 
        self.frame.destroy()
        if(self.closeFunction != None):
            self.closeFunction()

    def __init__(self, root, doneFunction, closeFunction = None):
        """
        :description: Create all the widgets for a file selection menu and display it to the user
        :return: The constructed class
        :rtype: FileSelect
        """ 

        if FileSelect.frame != None: #clear any old popups
            FileSelect.frame.destroy()

        FileSelect.frame = tk.Toplevel(root) # window
        FileSelect.frame.title(FileSelect.WINDOW_NAME)

        #create selected label
        self.selectedLabel = tk.Label(self.frame, text = FileSelect.SELECTED_TEXT, font = ("", 0, "bold"))
        self.selectedLabel.grid(column=0, row = 0)

        #create label to show filename
        self.fileLabel = tk.Label(self.frame, text = FileSelect.INITIAL_FILE_TEXT)
        self.fileLabel.grid(column=1, row = 0, pady = 5)

        #create button to open file dialogue
        self.selectionButton = tk.Button(self.frame, text = FileSelect.BUTTON_TEXT, width = 8, height = 0, command = self.select_file)
        self.selectionButton.grid(column = 0, row = 1)

        #create button to finish file selection
        self.doneButton = tk.Button(self.frame, text = FileSelect.DONE_TEXT, width = 8, height = 0, state = "disabled", command = doneFunction )
        self.doneButton.grid(column = 1, row = 1, pady = 5)

        #disable resizing
        self.frame.resizable(False, False) 

        #set closing callback function if specified
        if(closeFunction != None):
            self.closeFunction = closeFunction
            self.frame.protocol("WM_DELETE_WINDOW", self.runCloseFunction)

        FileSelect.frame.grab_set() # grab focus
