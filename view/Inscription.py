

import tkinter as tk
from tkinter import font
from control.controller import Controller
from view.connection import Connection
from view.placeholderEntry import PlaceholderEntry


class Inscription:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        controller = Controller(None)  # Controller should be instantiated before Inscription
        self.initialize_ui()

    def initialize_ui(self):
        self.root.title("MazeBank - Inscription")
        self.root.geometry("430x600")  
        self.root.configure(background='#f5f5f5')

    
        self.logo = tk.PhotoImage(file="assets/logo.png").subsample(2)  
        self.logo_label = tk.Label(self.root, image=self.logo, bg='#f5f5f5')
        self.logo_label.pack(pady=20)
        self.custom_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.title_label = tk.Label(self.root, text="MAZE BANK", font=self.custom_font, bg='#f5f5f5', fg='black')
        self.title_label.pack()

        # Titre "Inscription" en rouge
        self.inscription_title = tk.Label(self.root, text="Inscription", font=('Arial', 18, 'bold'), bg='#f5f5f5', fg='#DB0000')
        self.inscription_title.pack(pady=10)

        # Boîtes à remplir avec placeholder
        self.nom_entry = PlaceholderEntry(self.root, "Nom", font=('Arial', 12), bg='white', fg='black')
        self.nom_entry.pack(pady=5)

        self.prenom_entry = PlaceholderEntry(self.root, "Prénom", font=('Arial', 12), bg='white', fg='black')
        self.prenom_entry.pack(pady=5)

        self.email_entry = PlaceholderEntry(self.root, "Email", font=('Arial', 12), bg='white', fg='black')
        self.email_entry.pack(pady=5)

        self.mdp_entry = PlaceholderEntry(self.root, "", font=('Arial', 12), bg='white', fg='black', show='*')
        self.mdp_entry.pack(pady=5)


        self.inscription_button = tk.Button(self.root, text="S'inscrire", command=self.register, font=('Arial', 14), bg='white', fg='#DB0000', padx=20, pady=10, bd=0, activebackground='#FF5733', activeforeground='white')
        self.inscription_button.pack(pady=10)

        self.connection_button = tk.Button(self.root, text="Se connecter", command=self.go_to_connection, font=('Arial', 14), bg='#DB0000', fg='#DB0000', padx=20, pady=10, bd=0, activebackground='#FF5733', activeforeground='white')
        self.connection_button.pack(pady=10)
    
    
    def register(self):
        firstname = self.prenom_entry.get()
        name = self.nom_entry.get()
        email = self.email_entry.get()
        password = self.mdp_entry.get()
        self.controller.register_user(name, firstname, email, password)


    def go_to_connection(self):
        self.root.destroy()  #shot down the main window
        root = tk.Tk()
        controller = Controller(None)  # Controller should be instantiated before Inscription
        app = Connection(root, controller)
        app.create_widgets()
        app.run_connection()
        
if __name__ == "__main__":
    root = tk.Tk()
    controller = Controller(None)  # Controller should be instantiated before Inscription
    app = Inscription(root, controller)
    root.mainloop()