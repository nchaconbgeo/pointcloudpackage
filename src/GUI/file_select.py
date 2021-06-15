import tkinter as tk
from tkinter import filedialog

class FileSelect:
    """
    :Description: window to allow the user to select a file from their filesystem along with its exact format
    """ 

    frame = None
    selectedFile = ""
    selectionButton = None

    selectedLabel = None
    fileLabel = None
    formatLabel = None

    closeFunction = None

    formatEntry = None

    FORMAT_TEXT = "Format:"
    BUTTON_TEXT = "Select File"
    WINDOW_NAME = "Import File"
    SELECTED_TEXT = "Selected File:"
    INITIAL_FILE_TEXT = "None"
    DONE_TEXT = "Done"
    ENTRY_WIDTH = 25
    BUTTON_WIDTH = 8

    def select_file(self):
        """
        :Description: prompt the user to select a file from their filesystem
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

        if(selectedFile == None or selectedFile == () or selectedFile == ''):
            return #user cancelled selection operation

        self.selectedFile = selectedFile
        self.fileLabel.config(text = self.selectedFile)
        self.doneButton.config(state = "normal")

    def runCloseFunction(self):
        """
        :Description: run the specified callback function when the window is closed
        """ 
        self.frame.destroy()
        if(self.closeFunction != None):
            self.closeFunction()

    def __init__(self, root, doneFunction, closeFunction = None):
        """
        :Description: Create all the widgets for a file selection menu and display it to the user
        :return: FileSelect
        """ 

        if self.frame != None: #clear any old popups
            self.frame.destroy()

        self.frame = tk.Toplevel(root) # window
        self.frame.title(FileSelect.WINDOW_NAME)


        #create selected label
        self.selectedLabel = tk.Label(self.frame, text = FileSelect.SELECTED_TEXT, font = ("", 0, "bold"))
        self.selectedLabel.grid(column=0, row = 0)

        #create label to show filename
        self.fileLabel = tk.Label(self.frame, text = FileSelect.INITIAL_FILE_TEXT)
        self.fileLabel.grid(column=1, row = 0, pady = 5)

        #create button to open file dialogue
        self.selectionButton = tk.Button(self.frame, text = FileSelect.BUTTON_TEXT, width = 8, height = 0, command = self.select_file)
        self.selectionButton.grid(column = 0, row = 2)

        #create button to finish file selection
        self.doneButton = tk.Button(self.frame, text = FileSelect.DONE_TEXT, width = FileSelect.BUTTON_WIDTH, height = 0, state = "disabled", command = doneFunction )
        self.doneButton.grid(column = 1, row = 2, pady = 5)

        #create label for format entry box
        self.formatLabel = tk.Label(self.frame, text=FileSelect.FORMAT_TEXT, font = ("", 0, "bold"))
        self.formatLabel.grid(column=0, row=1)

        #create entry field for file format
        self.formatEntry = tk.Entry(self.frame, width=FileSelect.ENTRY_WIDTH)
        self.formatEntry.grid(column=1, row=1)

        

        #disable resizing
        self.frame.resizable(False, False) 

        #set closing callback function if specified
        if(closeFunction != None):
            self.closeFunction = closeFunction
            self.frame.protocol("WM_DELETE_WINDOW", self.runCloseFunction)

        self.frame.grab_set() # grab focus
