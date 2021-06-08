import tkinter as tk

class HomeScreen:

    frame = None

    homeLabel = None

    labelButton = None
    selectVolumeButton = None
    drawLineButton = None
    exportButton = None

    VIEW_LABEL_TEXT = "Edit/View Labels"
    SELECT_VOLUME_TEXT = "Select Volume"
    DRAW_LINE_TEXT = "Draw Line"
    EXPORT_TEXT = "Render/Export"



    def __init__(self, root, closeFunction = None):

        #adds label button to grid
        self.labelButton = tk.Button(self.frame, text=self.VIEW_LABEL_TEXT)
        self.labelButton.grid(row=1, column=0, pady=5, padx=5)

        #adds drawLine button to grid
        self.drawLineButton = tk.Button(self.frame, text=self.DRAW_LINE_TEXT)
        self.drawLineButton.grid(row = 1, column=1, padx=5)

        #adds select volume button to grid
        self.selectVolumeButton = tk.Button(self.frame, text=self.SELECT_VOLUME_TEXT)
        self.selectVolumeButton.grid(row = 2, column=0, padx=5, pady=5)

        #adds export button to grid
        self.exportButton = tk.Button(self.frame, text=self.EXPORT_TEXT)
        self.exportButton.grid(row = 2, column=1, padx=5)

# creates a Tk() object

root = tk.Tk()

h = HomeScreen(root)
tk.mainloop() 