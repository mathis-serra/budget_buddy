import tkinter as tk
from tkinter import font
import subprocess
from view.Inscription import Inscription
from view.Connection import Connection  # Importe le fichier connexion.py
from control.Controller import Controller

class Home:
    def __init__(self, root):
        self.root = root
        self.root.title("MazeBank")
        self.root.geometry("430x800") 
        self.root.configure(background='#f5f5f5')
        
        self.logo = tk.PhotoImage(file="assets/logo.png").subsample(2)  # Changer le facteur de sous-échantillonnage selon votre besoin
        self.logo_label = tk.Label(self.root, image=self.logo, bg='#f5f5f5')
        self.logo_label.pack(pady=20)

        self.custom_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.title_label = tk.Label(self.root, text="MAZE BANK", font=self.custom_font, bg='#f5f5f5', fg='black')
        self.title_label.pack()

        # home Message 
        message_lines = [
            "Veuillez vous inscrire pour créer un nouveau compte,",
            "ou si vous êtes déjà client, veuillez vous connecter."
        ]

        for line in message_lines:
            label = tk.Label(self.root, text=line, font=('Arial', 12), bg='#f5f5f5', fg='black')
            label.pack()

        # Bouton d'inscription
        self.inscription_button = tk.Button(self.root, text="S'inscrire", command=self.go_to_inscription, font=('Arial', 14), bg='#DB0000', fg='red', padx=20, pady=10, bd=0, activebackground='#FF5733', activeforeground='red')
        self.inscription_button.pack(pady=10)

        self.connection_button = tk.Button(self.root, text="Se connecter", command=self.go_to_connection, font=('Arial', 14), bg='#DB0000', fg='red', padx=20, pady=10, bd=0, activebackground='#FF5733', activeforeground='red')
        self.connection_button.pack(pady=10)

    def go_to_inscription(self):
        self.root.destroy()
        root = tk.Tk()
        controller = Controller(None)  
        Inscription(root, controller)
        

    def go_to_connection(self):
        self.root.destroy()  
        root = tk.Tk()
        controller = Controller(None)  
        Connection(root, controller)
        


