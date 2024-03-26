import re
import tkinter as tk

class Connection:
    def __init__(self):
        self.email_text = ""
        self.password_text = ""
        self.error_email = ""
        self.error_password = ""
        self.root = tk.Tk()
        self.root.geometry("800x600")

    def verify_email(self):
        email_input = self.email_text.get()
        if email_input:
            if "@" in email_input and "." in email_input:
                # Vérification de l'unicité de l'email
                if email_input == self.retreview_email(): # Attention, cette méthode n'est pas définie dans le code donné
                    return True
                else:
                    self.error_email = "Vous n'avez pas de compte avec cette email"
                    return False
            else:
                self.error_email = "Je ne comprend pas l'email saisie, veuillez réessayer"
                return False
        else:
            self.error_email = "Veuillez saisir un email"
            return False

    def verify_password(self):
        password_input = self.password_text.get()
        if password_input:
            if len(password_input) < 10:
                self.error_password = "Mot de passe trop court"
                return False
            if not re.search(r"[A-Z]", password_input):
                self.error_password = "Le mot de passe doit contenir une majuscule"
                return False
            if not re.search(r"[a-z]", password_input):
                self.error_password = "Le mot de passe doit contenir une minuscule"
                return False
            if not re.search(r"\d", password_input):
                self.error_password = "Le mot de passe doit contenir au moins un chiffre"
                return False
            if not re.search(r"[!@#$%^&*()-_+=]", password_input):
                self.error_password = "Un caractère spécial requis"
                return False
            return True
        self.error_password = "Veuillez saisir votre mot de passe" 
        return False

    def button_clicked(self):
        if self.verify_email() and self.verify_password():
            #self.home.home()
            pass
        else:
            pass

    def run(self):
        self.root.mainloop()


