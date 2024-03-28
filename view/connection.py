import tkinter as tk
from tkinter import font, Label, Button, messagebox
from view.placeholderEntry import PlaceholderEntry
from controller.con_user import Con_user

class Connection(PlaceholderEntry):
    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.con_user = Con_user()
        self.root.title("MazeBank - Inscription")
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

        self.connexion_button = Button(self.root, text="Se connecter", command=self.con_user.button_clicked, font=('Arial', 14), bg='red', fg='white', padx=20, pady=10, bd=0, activebackground='#FF5733', activeforeground='white')
        self.connexion_button.pack(pady=10)
        
    def run(self):
        self.root.mainloop()
        

    
