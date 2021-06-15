import tkinter as tk
from ClassificationMenu import ClassificationMenu

def closeRoot():
    root.destroy()

# creates a Tk() object
root = tk.Tk()
root.withdraw()
menu = ClassificationMenu(root, closeFunction = closeRoot)
  
# mainloop, runs infinitely
tk.mainloop()