import tkinter as tk
from Menu import Menu
from Inscription import Inscription
from Connexion import Connexion

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("MazeBank")
        self.root.geometry("430x600")
        self.root.configure(background='#f5f5f5')

        self.current_frame = None

        self.menu_frame = Menu(root, self.show_inscription, self.show_connexion)
        self.inscription_frame = Inscription(root, self.show_menu)
        self.connexion_frame = Connexion(root)

        self.show_menu()

    def show_menu(self):
        self.clear_frame()
        self.menu_frame.pack(fill="both", expand=True)
        self.current_frame = self.menu_frame

    def show_inscription(self):
        self.clear_frame()
        self.inscription_frame.pack(fill="both", expand=True)
        self.current_frame = self.inscription_frame

    def show_connexion(self):
        self.clear_frame()
        self.connexion_frame.pack(fill="both", expand=True)
        self.current_frame = self.connexion_frame

    def clear_frame(self):
        if self.current_frame:
            self.current_frame.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
