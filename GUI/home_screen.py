import tkinter as tk
import webbrowser
import application

class HomeScreen:
    """
    :Description: Class to manage allow user to access most other functionalities, like viewing, volume select, classification menu, exporting, drawing lines. 
    :interracts with: ClassificationMenu, PointData, Visualizer
    """ 
    app = None

    root = None
    frame = None

    homeLabel = None

    labelButton = None
    selectVolumeButton = None
    openVisualizerButton = None
    drawLineButton = None
    exportButton = None
    helpButton = None

    windowTitle = None

    closeFunction = None

    classificationMenu = None

    exportMenu = None

    WINDOW_NAME = "GeoPointClouds"

    TITLE_NAME = "GeoPointClouds -- 3D Visualization Software"

    VIEW_LABEL_TEXT = "Edit/View Labels"
    SELECT_VOLUME_TEXT = "Select Volume"
    DRAW_LINE_TEXT = "Draw Line"
    EXPORT_TEXT = "Render/Export"
    OPEN_VISUALIZER_TEXT = "View Point Cloud"

    HELP_TEXT = "?"
    HELP_SITE = "https://github.com/nchaconbgeo/pointcloudpackage"
    BUTTON_WIDTH = 14

    def openClassificationMenu(self):
        """
        :Description: open classification menu for labeling
        """ 
        import GUI.Classification.classification_menu
        self.classificationMenu = GUI.Classification.classification_menu.ClassificationMenu(self.root, self.app)

    def openExportMenu(self):
        """
        :Description: open export menu for image/point cloud export
        """ 
        import GUI.export_menu
        #TODO: EXPORT SEPARATE 
        self.exportMenu = GUI.export_menu.ExportMenu(self.root, self.app, exportPng=self.app.exportPng, exportRecolored=self.app.exportRecolored, exportSeparate=self.app.exportSeparate)


    def openHelpSite(self):
        webbrowser.open(HomeScreen.HELP_SITE, new=1)        
    
    def runCloseFunction(self):
        """
        :Description: run the callback function if the user exits out of the window, if it's been set
        """ 
        self.frame.destroy()
        if(self.closeFunction != None):
            self.closeFunction()

    def __init__(self, root, app, closeFunction = None):
        """
        :Description: Create all the widgets for the home screen and display it to the user
        :return: HomeScreen
        """ 
        self.root = root
        self.app = app
        self.frame = tk.Toplevel(root) # window
        self.frame.title(HomeScreen.WINDOW_NAME)

        #add window title
        self.windowTitle = tk.Label(self.frame, text = HomeScreen.TITLE_NAME)
        self.windowTitle.grid(row = 0, column = 0, columnspan = 2, padx = 8, pady = 5)

        #adds label button to grid
        self.labelButton = tk.Button(self.frame, text=self.VIEW_LABEL_TEXT, width = HomeScreen.BUTTON_WIDTH, command = self.openClassificationMenu)
        self.labelButton.grid(row=1, column=0, pady=5, padx=5)

        #adds drawLine button to grid
        self.drawLineButton = tk.Button(self.frame, text=self.DRAW_LINE_TEXT, width = HomeScreen.BUTTON_WIDTH, command = self.app.drawLine)
        self.drawLineButton.grid(row = 1, column=1, padx=5)

        #adds select volume button to grid
        self.selectVolumeButton = tk.Button(self.frame, text=self.SELECT_VOLUME_TEXT, width = HomeScreen.BUTTON_WIDTH, command = self.app.startVolumeSelector)
        self.selectVolumeButton.grid(row = 2, column=0, padx=5, pady=5)

        #adds open visualizer button to grid
        self.openVisualizerButton = tk.Button(self.frame, text=self.OPEN_VISUALIZER_TEXT, width = HomeScreen.BUTTON_WIDTH, command = self.app.startViewer)
        self.openVisualizerButton.grid(row = 3, column=0, padx=5, pady=5)

        #adds export button to grid
        self.exportButton = tk.Button(self.frame, text=self.EXPORT_TEXT, width = HomeScreen.BUTTON_WIDTH, command = self.openExportMenu)
        self.exportButton.grid(row = 2, column=1, padx=5)
        
        self.helpButton = tk.Button(self.frame, text=self.HELP_TEXT, command = self.openHelpSite)
        self.helpButton.grid(row = 3, column=1, sticky="E")

        #disable resizing
        self.frame.resizable(False, False) 

        #add close callback
        if(closeFunction != None):
            self.closeFunction = closeFunction
            self.frame.protocol("WM_DELETE_WINDOW", self.runCloseFunction)


if __name__ == "__main__" :
    root = tk.Tk()
    h = HomeScreen(root)
    tk.mainloop() 