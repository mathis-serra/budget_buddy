import re
from tkinter import messagebox
from view.connection import Connection
from view.Account import Account
from controller.sql_manager import SqlManager

class Con_user(SqlManager):
    def __init__(self):
        super().__init__()
        self.connection = Connection()
        self.email_user = self.connection.email_entry
        self.password_user = self.connection.password_entry

    def verify_email(self, email_input):
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

    def verify_password(self, password_input):
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
        if self.verify_email(self.email_user.get()) and self.verify_password(self.password_user.get()):
            account = Account()
            account.run()
        else:
            messagebox.showerror("Erreur", "Vous n'avez pas de compte. Inscrivez-vous")

    def run(self):
        self.connection.root.mainloop()
