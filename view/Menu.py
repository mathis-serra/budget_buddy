import tkinter as tk
from tkinter import font, messagebox
from control.Controller import Controller

class Menu:
    
    def __init__(self, root, user_info):
        self.root = root
        self.user_info = user_info
        self.controller = Controller(None)  
        self.transactions = []  # Initialize an empty list to store transactions
        self.create_widgets()
        
    def create_widgets(self):
        # Set the title of the window
        self.root.title("MazeBank")
        self.root.geometry("430x800")  
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
        
        # Get the initial balance of the account in the db 
        initial_balance = self.controller.get_balance(self.user_info['id'])
        self.account_balance = tk.Label(self.root, text=f"Solde:{initial_balance} € ", font=('Arial', 16), bg='#f5f5f5', fg='black')
        self.account_balance.pack(pady=5)
        
        # Add a label for the transactions

        # Add an imput field to enter the amount to deposit
        self.deposit_amount_entry = tk.Entry(self.root, font=('Arial', 12))
        self.deposit_amount_entry.pack(pady=5)

        self.deposit_button = tk.Button(self.root, text="Déposer", command=self.deposit, font=('Arial', 14), bg='#4CAF50', fg='red', padx=20, pady=10, bd=0, activebackground='#45a049', activeforeground='red')
        self.deposit_button.pack(pady=10)
        
        
        self.withdraw_button = tk.Button(self.root, text="Retirer", command=self.withdraw, font=('Arial', 14), bg='#f44336', fg='red', padx=20, pady=10, bd=0, activebackground='#f44336', activeforeground='red')
        self.withdraw_button.pack(pady=10)
        
        
        self.receiver_id = tk.Entry(self.root, font=('Arial', 12))
        self.receiver_id.pack(pady=5)
        
        self.amount = tk.Entry(self.root, font=('Arial', 12))
        self.amount.pack(pady=5)
        

        self.transfer_button = tk.Button(self.root, text="Virement", command=self.transfer, font=('Arial', 14), bg='#2196F3', fg='red', padx=20, pady=10, bd=0, activebackground='#2196F3', activeforeground='red')
        self.transfer_button.pack(pady=10)

        self.transaction_label = tk.Label(self.root, text="Transactions:", font=('Arial', 16, 'bold'), bg='#f5f5f5', fg='black')
        self.transaction_label.pack(pady=10)

        self.transaction_text = tk.Text(self.root, font=('Arial', 12), height=10, width=40)
        self.transaction_text.pack(pady=5)
        
        transactions = self.controller.get_transactions(self.user_info['id'])
        if transactions:
            self.display_transactions(transactions)
        

    #Deposit method to add money to the account
    def deposit(self):
        #Get the amount to deposit
        amount = float(self.deposit_amount_entry.get())
        self.controller.update_balance(self.user_info['id'], amount)
        self.transactions.append(f"Dépôt: +{amount} €") 
        self.controller.register_transaction( "Dépôt", self.user_info['id'], amount)
        self.update_transaction_text()
        balance = self.controller.get_balance(self.user_info['id'])
        self.account_balance.config(text=f"Solde: {balance} €")
        messagebox.showinfo("Dépôt effectué", f"Vous avez déposé {amount} € dans votre compte.")

    #Withdraw method to remove money from the account
    def withdraw(self):
        amount_entry = self.deposit_amount_entry.get()
        if amount_entry:
            amount = float(amount_entry)
        else:
            messagebox.showerror("Erreur de saisie", "Veuillez entrer un montant valide.")
        balance = self.controller.get_balance(self.user_info['id'])
        if amount > balance:
            messagebox.showerror("Solde insuffisant", "Vous n'avez pas assez d'argent sur votre compte.")
        else:
            #Update the balance
            self.controller.update_balance(self.user_info['id'], -amount)
            self.transactions.append(f"Retrait: -{amount} €")
            self.transaction_text.tag_configure("red", foreground="red")
            #Turn the withdraw transaction text red
            self.transaction_text.insert(tk.END, f"Retrait: -{amount} €", "red")
            self.controller.register_transaction( "Retrait", self.user_info['id'], amount)
            self.update_transaction_text()
            balance = self.controller.get_balance(self.user_info['id'])
            self.account_balance.config(text=f"Solde: {balance} €")
            messagebox.showinfo("Retrait effectué", f"Vous avez retiré {amount} € de votre compte.")
            
    #Update the transaction text area
    def update_transaction_text(self):
        self.transaction_text.delete('1.0', tk.END) 
        for transaction in self.transactions:
            self.transaction_text.insert(tk.END, transaction + "\n") 
    
        
    def transfer(self):
      
        receiver_id = int(self.receiver_id.get())  
        amount = float(self.amount.get())  
        
        success = self.controller.transfer(self.user_info['id'], receiver_id, amount)
        if success:
            self.withdraw()
            self.transaction_text.insert(tk.END, f"Retrait: -{amount} €", "red")
            self.controller.register_transaction( "Virement Sortant", self.user_info['id'], amount)
            messagebox.showinfo("Virement effectué", f"Vous avez transféré {amount} € au compte {receiver_id}.")
        else:
            messagebox.showerror("Échec du virement", "Impossible de traiter le virement. Veuillez vérifier votre solde ou le numéro de compte du destinataire.")

    
    def display_transactions(self, transactions):
        for transaction in transactions:
            reason = transaction['reason']
            amount = transaction['amount']
            self.transaction_text.insert(tk.END, f"{reason}: {amount} €\n")

    
    
    
    
