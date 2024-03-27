from tkinter import font
import placeholderEntry as PlaceholderEntry
import re
import tkinter as tk
from databases.sql_manager import SqlManager


class Connection(SqlManager, PlaceholderEntry):
    def __init__(self):
        SqlManager.__init__(self)
        PlaceholderEntry.__init__(self)
        self.error_email = ""
        self.error_password = ""
        self.root = tk.Tk()
        self.root.title("MazeBank - Inscription")
        self.root.geometry("430x600")  # Dimensions de la fenêtre
        self.root.configure(background='#f5f5f5')
        self.create_widgets()

    def create_widgets(self):
        # Redimensionnement du logo
        self.logo = tk.PhotoImage(file="logo.png").subsample(2)  # Changer le facteur de sous-échantillonnage selon votre besoin
        self.logo_label = tk.Label(self.root, image=self.logo, bg='#f5f5f5')
        self.logo_label.pack(pady=20)

        self.custom_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.title_label = tk.Label(self.root, text="MAZE BANK", font=self.custom_font, bg='#f5f5f5', fg='black')
        self.title_label.pack()

        self.connexion_title = tk.Label(self.root, text="Connexion", font=('Arial', 18, 'bold'), bg='#f5f5f5', fg='#DB0000')
        self.connexion_title.pack(pady=10)

        self.email_entry = PlaceholderEntry.PlaceholderEntry(self.root, "Email", font=('Arial', 12), bg='white', fg='black')
        self.email_entry.pack(pady=5)

        self.password_entry = PlaceholderEntry.PlaceholderEntry(self.root, "Mot de passe", font=('Arial', 12), bg='white', fg='black')
        self.password_entry.pack(pady=5)

        self.connexion_button = tk.Button(self.root, text="Se connecter", command=self.button_clicked, font=('Arial', 14), bg='red', fg='white', padx=20, pady=10, bd=0, activebackground='#FF5733', activeforeground='white')
        self.connexion_button.pack(pady=10)

    def verify_email(self):
        email_input = self.email_entry.get()
        if email_input:
            if "@" in email_input and "." in email_input:
                # Vérification de l'unicité de l'email
                if email_input == self.retreview_email():  # Attention, cette méthode n'est pas définie dans le code donné
                    return True
                else:
                    self.error_email = "Vous n'avez pas de compte avec cette adresse e-mail"
                    return False
            else:
                self.error_email = "Je ne comprends pas l'adresse e-mail saisie, veuillez réessayer"
                return False
        else:
            self.error_email = "Veuillez saisir une adresse e-mail"
            return False

    def verify_password(self):
        password_input = self.password_entry.get()
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
                self.error_password = "Un caractère spécial est requis"
                return False
            return True
        self.error_password = "Veuillez saisir votre mot de passe"
        return False

    def button_clicked(self):
        if self.verify_email() and self.verify_password():
            # self.home.home()
            pass
        else:
            print("vous n'avez pas de compte. Inscrivez vous")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Connection()
    app.run()
