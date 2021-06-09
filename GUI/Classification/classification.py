import tkinter as tk

class Classification:
    cloud_id = 0
    cloud_count = 0

    color = '#ff00ff'   #default color = obnoxious magenta
    name = 'New Classification'
    description = ''

    def __init__(self, name = 'Default Classification', description = 'Default Classification description', color = "#ff00ff"):
        self.cloud_id = Classification.cloud_count
        Classification.cloud_count += 1
        self.name = name
        self.description = description
        self.color = color

    def __str__(self):
        return str(self.name) + ": " + str(self.description) + ", color: " + self.color

classifications = []
