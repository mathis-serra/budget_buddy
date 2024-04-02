import tkinter as tk
from tkinter import font, ttk, messagebox
from tkcalendar import Calendar
import matplotlib.pyplot as plt
import numpy as np
from control.controller import Controller   

class Menu:
    
    def __init__(self, root, user_info):
        self.root = root
        self.user_info = user_info
        self.controller = Controller(None)  # Initialize controller for further use
        self.create_widgets()
        
    def create_widgets(self):
        
        
        self.root.title("MazeBank")
        self.root.geometry("430x600")  # Change window dimensions
        self.root.configure(background='#f5f5f5')

        # Ajout du logo
        self.logo = tk.PhotoImage(file="assets/logo.png").subsample(3)
        self.logo_label = tk.Label(self.root, image=self.logo, bg='#f5f5f5')
        self.logo_label.pack(pady=5)

        # Ajout du titre "Bienvenue chez MazeBank"
        self.custom_font = font.Font(family="Helvetica", size=20, weight="bold")
        self.title_label = tk.Label(self.root, text="Bienvenue chez MazeBank", font=self.custom_font, bg='#f5f5f5', fg='black')
        self.title_label.pack(pady=2)

        # Ajout du titre "Compte individuel" et du numéro de compte
        self.account_title = tk.Label(self.root, text="Compte individuel", font=('Helvetica', 16, 'bold'), bg='#f5f5f5', fg='black')
        self.account_title.pack(pady=5)

        self.account_number = tk.Label(self.root, text=f"Numéro de compte: {self.user_info['id']}", font=('Arial', 12), bg='#f5f5f5', fg='black')
        self.account_number.pack(pady=5)

        self.account_holder = tk.Label(self.root, text=f"Titulaire(s): {self.user_info['firstname']} {self.user_info['name']}", font=('Arial', 16), bg='#f5f5f5', fg='black')
        self.account_holder.pack(pady=5)
        
        self.account_balance = tk.Label(self.root, text=f"Solde: {self.controller.get_balance(self.user_info['id'])} €", font=('Arial', 16), bg='#f5f5f5', fg='black')
        self.account_balance.pack(pady=5)

        
        # Ajout du séparateur
        self.separator = ttk.Separator(self.root, orient='horizontal')
        self.separator.pack(fill='x', pady=10)
        
        # Ajout des boutons
        
        self.deposit_amount_entry = tk.Entry(self.root, font=('Arial', 12))
        self.deposit_amount_entry.pack(pady=5)

        self.deposit_button = tk.Button(self.root, text="Déposer", command=self.deposit, font=('Arial', 14), bg='#4CAF50', fg='red', padx=20, pady=10, bd=0, activebackground='#45a049', activeforeground='red')
        self.deposit_button.pack(pady=10)
        
        # self.withdraw_button = tk.Button(self.root, text="Retirer", command=self.withdraw, font=('Arial', 14), bg='#4CAF50', fg='red', padx=20, pady=10, bd=0, activebackground='#45a049', activeforeground='red')
        # self.withdraw_button.pack(pady=10)
        
  
  
  
    def deposit(self):
        # Récupérer le montant entré par l'utilisateur
        amount = float(self.deposit_amount_entry.get())
        
        # Mettre à jour le solde du compte en appelant la méthode du contrôleur
        self.controller.update_balance(self.user_info['id'], amount)
        
        # Mettre à jour l'affichage du solde
        self.account_balance.config(text=f"Solde: {self.controller.get_balance(self.user_info['id'])} €")
        
        # Afficher un message de confirmation
        messagebox.showinfo("Dépôt effectué", f"Vous avez déposé {amount} € dans votre compte.")
            
            