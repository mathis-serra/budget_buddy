import tkinter as tk
from tkinter import font, messagebox
from control.controller import Controller

class Menu:
    
    def __init__(self, root, user_info):
        self.root = root
        self.user_info = user_info
        self.controller = Controller(None)  # Initialize controller for further use
        self.create_widgets()
        
    def create_widgets(self):
        self.root.title("MazeBank")
        self.root.geometry("430x600")  
        self.root.configure(background='#f5f5f5')

        self.logo = tk.PhotoImage(file="assets/logo.png").subsample(3)
        self.logo_label = tk.Label(self.root, image=self.logo, bg='#f5f5f5')
        self.logo_label.pack(pady=5)

        self.custom_font = font.Font(family="Helvetica", size=20, weight="bold")
        self.title_label = tk.Label(self.root, text="Bienvenue chez MazeBank", font=self.custom_font, bg='#f5f5f5', fg='black')
        self.title_label.pack(pady=2)

        self.account_title = tk.Label(self.root, text="Compte individuel", font=('Helvetica', 16, 'bold'), bg='#f5f5f5', fg='black')
        self.account_title.pack(pady=5)

        self.account_number = tk.Label(self.root, text=f"Numéro de compte: {self.user_info['id']}", font=('Arial', 12), bg='#f5f5f5', fg='black')
        self.account_number.pack(pady=5)

        self.account_holder = tk.Label(self.root, text=f"Titulaire(s): {self.user_info['firstname']} {self.user_info['name']}", font=('Arial', 16), bg='#f5f5f5', fg='black')
        self.account_holder.pack(pady=5)
        
        initial_balance = self.controller.get_balance(self.user_info['id'])
        self.account_balance = tk.Label(self.root, text=f"Solde:{initial_balance} € ", font=('Arial', 16), bg='#f5f5f5', fg='black')
        self.account_balance.pack(pady=5)

        self.deposit_amount_entry = tk.Entry(self.root, font=('Arial', 12))
        self.deposit_amount_entry.pack(pady=5)

        self.deposit_button = tk.Button(self.root, text="Déposer", command=self.deposit, font=('Arial', 14), bg='#4CAF50', fg='red', padx=20, pady=10, bd=0, activebackground='#45a049', activeforeground='red')
        self.deposit_button.pack(pady=10)
        
        self.withdraw_amount_entry = tk.Entry(self.root, font=('Arial', 12))
        self.withdraw_amount_entry.pack(pady=5)

        self.withdraw_button = tk.Button(self.root, text="Retirer", command=self.withdraw, font=('Arial', 14), bg='#f44336', fg='red', padx=20, pady=10, bd=0, activebackground='#f44336', activeforeground='red')
        self.withdraw_button.pack(pady=10)

    def deposit(self):
        amount = float(self.deposit_amount_entry.get())
        self.controller.update_balance(self.user_info['id'], amount)
        balance = self.controller.get_balance(self.user_info['id'])
        self.account_balance.config(text=f"Solde: {balance} €")
        messagebox.showinfo("Dépôt effectué", f"Vous avez déposé {amount} € dans votre compte.")

    def withdraw(self):
        amount = float(self.withdraw_amount_entry.get())  # Correction ici
        balance = self.controller.get_balance(self.user_info['id'])
        if amount > balance:
            messagebox.showerror("Solde insuffisant", "Vous n'avez pas assez d'argent sur votre compte.")
        else:
            self.controller.update_balance(self.user_info['id'], -amount)
            balance = self.controller.get_balance(self.user_info['id'])
            self.account_balance.config(text=f"Solde: {balance} €")
            messagebox.showinfo("Retrait effectué", f"Vous avez retiré {amount} € de votre compte.")
