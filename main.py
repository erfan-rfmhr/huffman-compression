from tkinter import Tk

from gui import App

if __name__ == "__main__":
    # Create root window
    root = Tk()
    # Create app
    app = App(root)
    # Start mainloop
    root.mainloop()