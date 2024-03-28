import re
import tkinter as tk
from tkinter import font, Label, Button, messagebox
from pages.placeholderEntry import PlaceholderEntry
from base.sql_manager import SqlManager
from pages.Account import Account
from tkinter import font
import pages.placeholderEntry as PlaceholderEntry
import re, tkinter as tk
# import databases.sql_manager as SqlManager


class Connection(SqlManager):
    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.root.title("MazeBank - Inscription")
        self.root.geometry("430x600")
        self.root.configure(background='#f5f5f5')
        self.create_widgets()

    def create_widgets(self):
        self.custom_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.title_label = Label(self.root, text="MAZE BANK", font=self.custom_font, bg='#f5f5f5', fg='black')
        self.title_label.pack()

        self.connexion_title = Label(self.root, text="Connexion", font=('Arial', 18, 'bold'), bg='#f5f5f5', fg='#DB0000')
        self.connexion_title.pack(pady=10)

        self.email_entry = PlaceholderEntry(self.root, "Email", font=('Arial', 12), bg='white', fg='black')
        self.email_entry.pack(pady=5)

        self.password_entry = PlaceholderEntry(self.root, "Mot de passe", font=('Arial', 12), bg='white', fg='black')
        self.password_entry.pack(pady=5)

        self.connexion_button = Button(self.root, text="Se connecter", command=self.button_clicked, font=('Arial', 14), bg='red', fg='white', padx=20, pady=10, bd=0, activebackground='#FF5733', activeforeground='white')
        self.connexion_button.pack(pady=10)

    def verify_email(self):
        email_input = self.email_entry.get()
        if email_input:
                # Vérification de l'unicité de l'email
                if email_input == self.retrieve_email():  # Assurez-vous que cette méthode récupère l'email depuis la base de données
                    return True
                else:
                    messagebox.showerror("Erreur", "Vous n'avez pas de compte avec cette adresse e-mail")
                    return False            
        else:
            messagebox.showerror("Erreur", "Veuillez saisir une adresse e-mail")
            return False

    def verify_password(self):
        password_input = self.password_entry.get()
        if password_input:
            if password_input == self.retrieve_password():  # Assurez-vous que cette méthode récupère le mot de passe depuis la base de données
                if len(password_input) < 10:
                    messagebox.showerror("Erreur", "Mot de passe trop court")
                    return False
                if not re.search(r"[A-Z]", password_input):
                    messagebox.showerror("Erreur", "Le mot de passe doit contenir une majuscule")
                    return False
                if not re.search(r"[a-z]", password_input):
                    messagebox.showerror("Erreur", "Le mot de passe doit contenir une minuscule")
                    return False
                if not re.search(r"\d", password_input):
                    messagebox.showerror("Erreur", "Le mot de passe doit contenir au moins un chiffre")
                    return False
                if not re.search(r"[!@#$%^&*()-_+=]", password_input):
                    messagebox.showerror("Erreur", "Un caractère spécial est requis")
                    return False
                return True
            else:
                messagebox.showerror("Erreur", "Veuillez saisir votre mot de passe")
                return False

    def button_clicked(self):
        if self.verify_email() and self.verify_password():
            account = Account()
            account.run()
        else:
            messagebox.showerror("Vous n'avez pas de compte. Inscrivez-vous")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    to_connect = Connection()
    to_connect.run()
