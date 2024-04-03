# from view.home import Menu
import tkinter as tk
from view.Home import Home


if __name__ == "__main__":
    root = tk.Tk()
    app = Home(root)
    root.mainloop()