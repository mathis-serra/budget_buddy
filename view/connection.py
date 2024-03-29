import tkinter as tk
from tkinter import font, Label
from view.placeholderEntry import PlaceholderEntry

class Connection(PlaceholderEntry):
    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.root.title("MazeBank - Connexion")
        self.root.geometry("430x600")
        self.root.configure(background='#f5f5f5')
        self.create_widgets()


    def create_widgets(self):
        self.custom_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.title_label = Label(self.root, text="MAZE BANK", font=self.custom_font, bg='#f5f5f5', fg='black')
        self.title_label.pack()

        self.connexion_title = Label(self.root, text="Connexion", font=('Arial', 18, 'bold'), bg='#f5f5f5', fg='#DB0000')
        self.connexion_title.pack(pady=10)

        self.email_entry = PlaceholderEntry(self.root, "Email", font=('Arial', 12), bg='white', fg='black')
        self.email_entry.pack(pady=5)

        self.password_entry = PlaceholderEntry(self.root, "Mot de passe", font=('Arial', 12), bg='white', fg='black')
        self.password_entry.pack(pady=5)        
        
    def run_connection(self):

        self.root.mainloop()
