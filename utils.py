import tkinter as tk
from tkinter import filedialog

def center_window(window, width, height): # This is a function to center a window on the screen
   window.update_idletasks()  # ensures geometry is calculated
    
    # Do NOT overwrite width and height
   screen_width = window.winfo_screenwidth()
   screen_height = window.winfo_screenheight()

   x = (screen_width // 2) - (width // 2)
   y = (screen_height // 2) - (height // 2)

   window.geometry(f"{width}x{height}+{x}+{y}")

def registerItems(base): # This is a function to register items
    register_window = tk.Toplevel(base) # Creates a new Tkinter window
    register_window.title("Register Items") 
    register_window.geometry("300x200")
    base.withdraw() # Hides the base window

def openFile(): # This is a function to open and loadt a file
    file_path= filedialog.askopenfilename() # Opens a file dialog to select a file
    return file_path