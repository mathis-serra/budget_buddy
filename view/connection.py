# connection.py

import tkinter as tk
from tkinter import font, Label, Button
from view.placeholderEntry import PlaceholderEntry
from control.controller import Controller
from view.Account import Menu

class Connection(PlaceholderEntry):
    def __init__(self, root, controller):
        super().__init__()
        self.controller = controller
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        self.root.title("MazeBank - Connexion")
        self.root.geometry("430x600")
        self.root.configure(background='#f5f5f5')

        self.logo = tk.PhotoImage(file="assets/logo.png").subsample(2)  
        self.logo_label = tk.Label(self.root, image=self.logo, bg='#f5f5f5')
        self.logo_label.pack(pady=20)
        self.custom_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.title_label = tk.Label(self.root, text="MAZE BANK", font=self.custom_font, bg='#f5f5f5', fg='black')
        self.title_label.pack()

        self.connexion_title = Label(self.root, text="Connexion", font=('Arial', 18, 'bold'), bg='#f5f5f5', fg='#DB0000')
        self.connexion_title.pack(pady=10)

        self.email_entry = PlaceholderEntry(self.root, "Email", font=('Arial', 12), bg='white', fg='black')
        self.email_entry.pack(pady=5)

        self.password_entry = PlaceholderEntry(self.root, "Mot de passe", font=('Arial', 12), bg='white', fg='black')
        self.password_entry.pack(pady=5)

        self.connexion_button = Button(self.root, text="Se connecter", command=self.login, font=('Arial', 14), bg='red', fg='white', padx=20, pady=10, bd=0, activebackground='#FF5733', activeforeground='white')
        self.connexion_button.pack(pady=10)
        
    def run_connection(self):
        self.root.mainloop()
    
    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        if self.controller.login_user(email, password):
            self.root.destroy()
            root = tk.Tk()
            app = Menu(root)
            root.mainloop()
