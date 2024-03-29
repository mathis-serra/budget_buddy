from modeles.sql_manager import SqlManager
from tkinter import messagebox

class Controller:
    def __init__(self, view):
        self.view = view
        self.model = SqlManager()

    def register_user(self, name, firstname, email, password):
        if name == "" or firstname == "" or email == "" or password == "":
            print("Veuillez remplir tous les champs")
        elif len(password) < 8:
            print("Le mot de passe doit contenir au moins 8 caractères")
        else:
            self.model.insert_user(name, firstname, email, password)
            print("Utilisateur enregistré avec succès")

    def login_user(self, email, password):
        if self.model.verify_user(email, password):
            print("Connexion réussie")
            return True
        else:
            print("Connexion échouée")
            return False