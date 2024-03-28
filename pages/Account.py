import tkinter as tk
from tkinter import font, messagebox

class Account:
    def __init__(self):
        self.root = tk.Tk()
class Account:
    def __init__(self, root):
        self.root = root
        self.root.title("MazeBank")
        self.root.geometry("430x600")
        self.root.configure(background='#f5f5f5')

        self.frame = tk.Frame(self.root, bg='#f5f5f5')
        self.frame.place(relx=0.5, rely=0.3, anchor='center')

        self.logo = tk.PhotoImage(file="logo.png").subsample(3)
        self.logo_label = tk.Label(self.frame, image=self.logo, bg='#f5f5f5')
        self.logo_label.pack(pady=5)

        self.custom_font = font.Font(family="Helvetica", size=20, weight="bold")
        self.title_label = tk.Label(self.frame, text="Bienvenue chez MazeBank", font=self.custom_font, bg='#f5f5f5', fg='black')
        self.title_label.pack(pady=2)

        self.create_account_info()

        self.separator = tk.Frame(self.frame, height=2, width=400, bg='black')  # Utilisation de tk.Frame
        self.separator.pack(fill='x', pady=10)

        self.create_buttons()

    def create_account_info(self):
        self.account_title = tk.Label(self.frame, text="Compte individuel", font=('Helvetica', 16, 'bold'), bg='#f5f5f5', fg='black')
        self.account_title.pack(pady=5)

        self.account_number = tk.Label(self.frame, text="Numéro de compte : 12345678", font=('Arial', 12), bg='#f5f5f5', fg='black')
        self.account_number.pack(pady=5)

        self.account_holder = tk.Label(self.frame, text="Titulaire(s): Nom Prénom", font=('Arial', 16), bg='#f5f5f5', fg='black')
        self.account_holder.pack(pady=5, anchor='w')

    def create_buttons(self):
        buttons_data = [
            ("Afficher le solde", self.show_balance),
            ("Rechercher des transactions", self.toggle_criteria),
            ("Récapitulatif", self.show_summary),
            ("Graphiques", self.show_graphs)
        ]

        for text, command in buttons_data:
            button = tk.Button(self.frame, text=text, command=command, font=('Arial', 14), bg='#4CAF50', fg='red', padx=20, pady=10, bd=0, activebackground='#45a049', activeforeground='red')
            button.pack(pady=10)

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

    # def run(self):
    #     self.root.mainloop()
    #     plt.figure(figsize=(6, 4))
    #     plt.bar(categories, expenses, color='skyblue')
    #     plt.xlabel('Catégories')
    #     plt.ylabel('Dépenses (€)')
    #     plt.title('Dépenses par catégorie')
    #     plt.xticks(rotation=45)
    #     plt.tight_layout()

    #     plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = Account(root)
    root.mainloop()
