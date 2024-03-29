# from view.home import Menu
from control.controller import Controller
import tkinter as tk

from view.Inscription import Inscription
# from control.con_user import Con_user


if __name__ == "__main__":
    root = tk.Tk()
    controller = Controller(None)  # Controller should be instantiated before Inscription
    app = Inscription(root, controller)
    root.mainloop()