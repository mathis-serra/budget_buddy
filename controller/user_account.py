from view.Account import Account
from tkinter import messagebox

class User_Account:
    def __init__(self):
        self.account = Account()
    
    def show_balance(self):
        balance = self.get_balance()
        messagebox.showinfo("Solde du compte", f"Votre solde actuel est de : {balance} €")

    def get_balance(self):
        # Simulation de récupération du solde depuis la base de données
        return 1000

    def toggle_criteria(self):
        messagebox.showinfo("Rechercher des transactions", "Fonctionnalité à implémenter")

    def show_summary(self):
        balance = self.get_balance()
        monthly_expenses = self.get_monthly_expenses()
        messagebox.showinfo("Récapitulatif", f"Solde actuel : {balance} €\nDépenses du mois : {monthly_expenses} €")

    def get_monthly_expenses(self):
        # Simulation de récupération des dépenses du mois depuis la base de données
        return 500

    def show_graphs(self):
        # Simulation de données pour les graphiques
        categories = ['Alimentation', 'Logement', 'Transport', 'Loisirs', 'Autres']
        expenses = [200, 300, 150, 100, 250]

        messagebox.showinfo("Graphiques", "Fonctionnalité à implémenter")
        
    def create_buttons(self):
        buttons_data = [
            ("Afficher le solde", self.show_balance),
            ("Rechercher des transactions", self.toggle_criteria),
            ("Récapitulatif", self.show_summary),
            ("Graphiques", self.show_graphs)
        ]

        for text, command in buttons_data:
            button = self.account.create_button(text, command)
            button.pack(pady=10)   

        