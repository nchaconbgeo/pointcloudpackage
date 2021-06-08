import tkinter as tk
import webbrowser

class HomeScreen:

    frame = None

    homeLabel = None

    labelButton = None
    selectVolumeButton = None
    drawLineButton = None
    exportButton = None
    helpButton = None

    windowTitle = None


    WINDOW_NAME = "GeoPointClouds"

    TITLE_NAME = "GeoPointClouds -- 3D Visualization Software"

    VIEW_LABEL_TEXT = "Edit/View Labels"
    SELECT_VOLUME_TEXT = "Select Volume"
    DRAW_LINE_TEXT = "Draw Line"
    EXPORT_TEXT = "Render/Export"

    HELP_TEXT = "?"
    HELP_SITE = "https://github.com/nchaconbgeo/pointcloudpackage"
    
    BUTTON_WIDTH = 14

    def openHelpSite(self):
        webbrowser.open(HomeScreen.HELP_SITE, new=1)        

    def __init__(self, root, closeFunction = None):
        self.frame = tk.Toplevel(root) # window
        self.frame.title(HomeScreen.WINDOW_NAME)

        #add window title
        self.windowTitle = tk.Label(self.frame, text = HomeScreen.TITLE_NAME)
        self.windowTitle.grid(row = 0, column = 0, columnspan = 2, padx = 8, pady = 5)

        #adds label button to grid
        self.labelButton = tk.Button(self.frame, text=self.VIEW_LABEL_TEXT, width = HomeScreen.BUTTON_WIDTH)
        self.labelButton.grid(row=1, column=0, pady=5, padx=5)

        #adds drawLine button to grid
        self.drawLineButton = tk.Button(self.frame, text=self.DRAW_LINE_TEXT, width = HomeScreen.BUTTON_WIDTH)
        self.drawLineButton.grid(row = 1, column=1, padx=5)

        #adds select volume button to grid
        self.selectVolumeButton = tk.Button(self.frame, text=self.SELECT_VOLUME_TEXT, width = HomeScreen.BUTTON_WIDTH)
        self.selectVolumeButton.grid(row = 2, column=0, padx=5, pady=5)

        #adds export button to grid
        self.exportButton = tk.Button(self.frame, text=self.EXPORT_TEXT, width = HomeScreen.BUTTON_WIDTH)
        self.exportButton.grid(row = 2, column=1, padx=5)
        
        self.helpButton = tk.Button(self.frame, text=self.HELP_TEXT, command = self.openHelpSite)
        self.helpButton.grid(row = 3, column=1, sticky="E")

        #disable resizing
        self.frame.resizable(False, False) 

# creates a Tk() object
root = tk.Tk()

h = HomeScreen(root)
tk.mainloop() 