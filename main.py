from view.Inscription import Inscription
from control.controller import Controller
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()
    controller = Controller(None)  # Controller should be instantiated before Inscription
    app = Inscription(root, controller)
    root.mainloop()
