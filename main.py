from pages.Inscription import Inscription
from pages.connection import Connection
from pages.home import Menu
import tkinter as tk
from pages.Account import Account

if __name__ == "__main__":
    root = tk.Tk()
    app = Menu(root)
    root.mainloop()
