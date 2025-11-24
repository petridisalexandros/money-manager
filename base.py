import tkinter as tk
from utils import openFile
from utils import registerItems
from utils import center_window

class MoneyManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        #Window configuration
        self.title("Money Manager")
        center_window(self, 600, 300)

        #Load icon
        self.icon = tk.PhotoImage(file = "/home/fuckoff/Documents/Projects/MoneyManager/icons/logo.png")
        self.iconphoto(True, self.icon)

        #Create UI
        self.create_widgets()

    def create_widgets(self):
        self.first_time_label = tk.Label(self, text="Is this your first time using the app?")
        self.first_time_label.pack(pady=10)

        #yes button
        self.yes_button = tk.Button(self, text="Yes", command=lambda: registerItems(self))
        self.yes_button.pack(pady=5)

        #No button
        self.no_button = tk.Button(self, text="No", command=openFile)
        self.no_button.pack(pady=5)   

        #Exit App Button
        self.exit_button = tk.Button(self, text="Exit App", command=self.destroy)
        self.exit_button.pack(pady=20)
if __name__ == "__main__":
    app = MoneyManagerApp()
    app.mainloop()