import application
import tkinter as tk

class ExportMenu:
    """
    :Description: Menu that contains the functionality for exporting different types of files. 
    :interracts with: Visualizer
    """ 

    WINDOW_NAME = "Export Type"

    frame = None
    root = None
    app = None

    #png, recolored point cloud (.txt)
    #separate point clouds 
    #original color point cloud with classification 


    exportPng = tk.IntVar()
    exportRecolored = tk.IntVar()
    exportSeparate = tk.IntVar()

    EXPORT_PNG_TEXT = "Export as .PNG"
    EXPORT_RECOLORED_TEXT = "Export Colored Point Cloud"
    EXPORT_SEPARATE_TEXT = "Export Each Classification Separately"

    EXPORT_TEXT = "Export"

    pngCheckButton = None
    recoloredCheckButton = None
    separateCheckButton = None
    
    exportButton = None

    def __init__(self, root, app, doneCommand):
        """
        :Description: Create the menu object that shows export options
        :param root: (tkinter.Tk) the root context to create the window in
        :param app: (application) the application, which holds the pointData
        :return: ExportMenu
        """ 
        self.root = root
        self.app = app
        
        self.frame = tk.Toplevel(root)
        self.frame.title(ExportMenu.WINDOW_NAME)

        label = tk.Label(self.frame, text = ExportMenu.WINDOW_NAME, font = ("", 0, "bold"))
        label.grid(row = 0, column = 0)
        
        self.pngCheckButton = tk.Checkbutton(self.frame, text = ExportMenu.EXPORT_PNG_TEXT, variable = self.exportPng)
        self.pngCheckButton.grid(row = 1, column = 0, sticky='W')

        self.recoloredCheckButton = tk.Checkbutton(self.frame, text = ExportMenu.EXPORT_RECOLORED_TEXT, variable = self.exportRecolored)
        self.recoloredCheckButton.grid(row = 2, column = 0, sticky='W')

        self.separateCheckButton = tk.Checkbutton(self.frame, text = ExportMenu.EXPORT_SEPARATE_TEXT, variable = self.exportSeparate)
        self.separateCheckButton.grid(row = 3, column = 0, sticky='W')

        self.exportButton = tk.Button(self.frame, text=ExportMenu.EXPORT_TEXT, command = doneCommand)
        self.exportButton.grid(row=4, column = 0, pady = 5)
        
        self.frame.grab_set()
        self.frame.resizable(False, False) #disable resizing window

