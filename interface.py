import tkinter as tk
from tkinter import font, ttk, messagebox
from tkcalendar import Calendar
import matplotlib.pyplot as plt
import numpy as np

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("MazeBank")
        self.root.geometry("430x600")  # Changement des dimensions de la fenêtre
        self.root.configure(background='#f5f5f5')

        self.frame = tk.Frame(self.root, bg='#f5f5f5')
        self.frame.pack(pady=50)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        # Ajout du logo
        self.logo = tk.PhotoImage(file="logo.png").subsample(3)
        self.logo_label = tk.Label(self.frame, image=self.logo, bg='#f5f5f5')
        self.logo_label.pack(pady=5)

        # Ajout du titre "Bienvenue chez MazeBank"
        self.custom_font = font.Font(family="Helvetica", size=20, weight="bold")
        self.title_label = tk.Label(self.frame, text="Bienvenue chez MazeBank", font=self.custom_font, bg='#f5f5f5', fg='black')
        self.title_label.pack(pady=2)

        # Ajout du titre "Compte individuel" et du numéro de compte
        self.account_title = tk.Label(self.frame, text="Compte individuel", font=('Helvetica', 16, 'bold'), bg='#f5f5f5', fg='black')
        self.account_title.pack(pady=5)

        self.account_number = tk.Label(self.frame, text="Numéro de compte : 12345678", font=('Arial', 12), bg='#f5f5f5', fg='black')
        self.account_number.pack(pady=5)

        # Ajout du titulaire du compte
        self.account_holder = tk.Label(self.frame, text="Titulaire(s): Nom Prénom", font=('Arial', 16), bg='#f5f5f5', fg='black')
        self.account_holder.pack(pady=5, anchor='w')

        # Ajout du séparateur
        self.separator = ttk.Separator(self.frame, orient='horizontal')
        self.separator.pack(fill='x', pady=10)

        # Ajout des boutons
        self.balance_button = tk.Button(self.frame, text="Afficher le solde", command=self.show_balance, font=('Arial', 14), bg='#4CAF50', fg='red', padx=20, pady=10, bd=0, activebackground='#45a049', activeforeground='red')
        self.balance_button.pack(pady=10)

        self.search_button = tk.Button(self.frame, text="Rechercher des transactions", command=self.toggle_criteria, font=('Arial', 14), bg='#4CAF50', fg='red', padx=20, pady=10, bd=0, activebackground='#45a049', activeforeground='red')
        self.search_button.pack(pady=10)

        self.criteria_options = ["Critère", "Date", "Catégorie", "Ressource", "Dépense", "Prix (Croissant)", "Prix (Décroissant)", "Entre deux dates"]
        self.combobox = ttk.Combobox(self.frame, values=self.criteria_options, state="readonly", font=('Arial', 12))
        self.combobox.current(0)
        self.combobox.bind("<<ComboboxSelected>>", self.handle_combobox_selection)

        self.validate_button = tk.Button(self.frame, text="Valider la recherche", command=self.validate_search, font=('Arial', 14), bg='#4CAF50', fg='red', padx=20, pady=10, bd=0, activebackground='#45a049', activeforeground='red')

        self.criteria_shown = False
        self.cal = None
        self.selected_dates = []

        self.summary_button = tk.Button(self.frame, text="Récapitulatif", command=self.show_summary, font=('Arial', 14), bg='#4CAF50', fg='red', padx=20, pady=10, bd=0, activebackground='#45a049', activeforeground='red')
        self.summary_button.pack(pady=10)

        self.graph_button = tk.Button(self.frame, text="Graphiques", command=self.show_graphs, font=('Arial', 14), bg='#4CAF50', fg='red', padx=20, pady=10, bd=0, activebackground='#45a049', activeforeground='red')
        self.graph_button.pack(pady=10)

    def show_balance(self):
        balance = self.get_balance()
        messagebox.showinfo("Solde du compte", f"Votre solde actuel est de : {balance} €")

    def get_balance(self):
        # Simulation de récupération du solde depuis la base de données
        # Pour cet exemple, nous allons simplement retourner un solde fictif
        return 1000

    def toggle_criteria(self):
        if self.criteria_shown:
            self.criteria_shown = False
            self.combobox.pack_forget()
            if self.cal:
                self.cal.pack_forget()
            self.validate_button.pack_forget()
        else:
            self.criteria_shown = True
            self.combobox.pack(pady=10)
            if self.combobox.get() in ["Date", "Entre deux dates"]:
                self.show_calendar()
            self.validate_button.pack(pady=10)

    def handle_combobox_selection(self, event):
        selected_criteria = self.combobox.get()
        if selected_criteria in ["Date", "Entre deux dates"]:
            self.show_calendar()
        else:
            if self.cal:
                self.cal.pack_forget()

    def show_calendar(self):
        if self.cal:
            self.cal.pack(pady=10)
        else:
            self.cal = Calendar(self.frame, selectmode="day", year=2024, month=3, day=23, date_pattern='yyyy-mm-dd')
            self.cal.pack(pady=10)
        if self.combobox.get() == "Entre deux dates":
            self.cal.bind("<<CalendarSelected>>", self.handle_date_selection)

    def handle_date_selection(self, event):
        date = self.cal.get_date()
        if len(self.selected_dates) < 2:
            self.selected_dates.append(date)
            messagebox.showinfo("Date sélectionnée", f"Date sélectionnée : {date}")
        if len(self.selected_dates) == 2:
            self.cal.unbind("<<CalendarSelected>>")
            self.cal.pack_forget()

    def validate_search(self):
        selected_criteria = self.combobox.get()

        if selected_criteria in ["Date", "Entre deux dates"]:
            if selected_criteria == "Date":
                selected_date = self.cal.get_date()
                messagebox.showinfo("Recherche", f"Recherche pour le critère '{selected_criteria}' : {selected_date}")
            elif selected_criteria == "Entre deux dates":
                if len(self.selected_dates) == 2:
                    messagebox.showinfo("Recherche", f"Recherche entre les dates : {self.selected_dates[0]} et {self.selected_dates[1]}")
                else:
                    messagebox.showerror("Erreur", "Veuillez sélectionner deux dates pour la recherche.")
        else:
            messagebox.showinfo("Recherche", f"Recherche pour le critère '{selected_criteria}'")

        self.criteria_shown = False
        self.combobox.pack_forget()
        self.validate_button.pack_forget()

    def show_summary(self):
        balance = self.get_balance()
        monthly_expenses = self.get_monthly_expenses()  # Ajout : Récupération des dépenses du mois
        messagebox.showinfo("Récapitulatif", f"Solde actuel : {balance} €\nDépenses du mois : {monthly_expenses} €")

    def get_monthly_expenses(self):
        # Simulation de récupération des dépenses du mois depuis la base de données
        # Pour cet exemple, nous allons simplement retourner un montant fictif
        return 500

    def show_graphs(self):
        # Simulation de données pour les graphiques
        categories = ['Alimentation', 'Logement', 'Transport', 'Loisirs', 'Autres']
        expenses = [200, 300, 150, 100, 250]

        plt.figure(figsize=(6, 4))
        plt.bar(categories, expenses, color='skyblue')
        plt.xlabel('Catégories')
        plt.ylabel('Dépenses (€)')
        plt.title('Dépenses par catégorie')
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()
