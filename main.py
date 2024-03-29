# from view.home import Menu
from control.controller import Controller
import tkinter as tk

from view.home import Home


if __name__ == "__main__":
    root = tk.Tk()
    app = Home(root)
    root.mainloop()