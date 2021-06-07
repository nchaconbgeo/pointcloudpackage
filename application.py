import tkinter as tk
from GUI import file_select
import import_export

class Application:
    root = None
    
    fileSelect = None


    def __init__(self):
        # creates a Tk() object
        self.root = tk.Tk()
        self.root.withdraw()
        self.fileSelect = file_select.FileSelect(self.root, self.doneSelectingFile, closeFunction = self.root.destroy)
        # mainloop, runs infinitely
        tk.mainloop()   

    def doneSelectingFile(self):
        #TODO
        import_export.txtToPcd()
        print(self.fileSelect.selectedFile)

app = Application()