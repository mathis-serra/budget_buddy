import tkinter as tk
from tkinter import font
import subprocess
from view.Inscription import Inscription
from view.connection import Connection  # Importe le fichier connexion.py
from control.controller import Controller

class Home:
    def __init__(self, root):
        self.root = root
        self.root.title("MazeBank")
        self.root.geometry("430x600")  # Nouvelles dimensions de la fenêtre
        self.root.configure(background='#f5f5f5')
        
        

        # Redimensionnement du logo
        self.logo = tk.PhotoImage(file="assets/logo.png").subsample(2)  # Changer le facteur de sous-échantillonnage selon votre besoin
        self.logo_label = tk.Label(self.root, image=self.logo, bg='#f5f5f5')
        self.logo_label.pack(pady=20)

        self.custom_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.title_label = tk.Label(self.root, text="MAZE BANK", font=self.custom_font, bg='#f5f5f5', fg='black')
        self.title_label.pack()

        # Phrase écrite ligne par ligne
        message_lines = [
            "Veuillez vous inscrire pour créer un nouveau compte,",
            "ou si vous êtes déjà client, veuillez vous connecter."
        ]

        for line in message_lines:
            label = tk.Label(self.root, text=line, font=('Arial', 12), bg='#f5f5f5', fg='black')
            label.pack()

        # Changement de couleur des boutons en rouge avec texte blanc
        self.inscription_button = tk.Button(self.root, text="S'inscrire", command=self.go_to_inscription, font=('Arial', 14), bg='#DB0000', fg='red', padx=20, pady=10, bd=0, activebackground='#FF5733', activeforeground='red')
        self.inscription_button.pack(pady=10)

        self.connection_button = tk.Button(self.root, text="Se connecter", command=self.go_to_connection, font=('Arial', 14), bg='#DB0000', fg='red', padx=20, pady=10, bd=0, activebackground='#FF5733', activeforeground='red')
        self.connection_button.pack(pady=10)

    def go_to_inscription(self):
        # Fermer la fenêtre du menu principal
        self.root.destroy()
        # Ouvrir la fenêtre d'inscription
        root = tk.Tk()
        controller = Controller(None)  # Controller should be instantiated before Inscription
        app = Inscription(root, controller)
        app.mainloop()

    def go_to_connection(self):
        self.root.destroy()  # Ferme la fenêtre du menu principal
        root = tk.Tk()
        controller = Controller(None)  # Controller should be instantiated before Inscription
        app = Connection(root, controller)
        # app.create_widgets()
        root.run()

if __name__ == "__main__":
    root = tk.Tk()
    app = Home(root)
    root.mainloop()
