from modeles.sql_manager import SqlManager


class Controller:
    def __init__(self, view):
        self.view = view
        # create an instance of the model
        self.model = SqlManager()
    # register a new user
    
    def register_user(self, name, firstname, email, password):
        if name == "" or firstname == "" or email == "" or password == "":
            print("Veuillez remplir tous les champs")
        elif len(password) < 8:
            print("Le mot de passe doit contenir au moins 8 caractères")
        else:
            self.model.insert_user(name, firstname, email, password)
            print("Utilisateur enregistré avec succès")
    # login a user
    def login_user(self, email, password):
        user_info = self.model.verify_user(email, password)
        if user_info:
            print("Connexion réussie")
            return user_info
        else:
            print("Connexion échouée")
            return None
    # get the balance of the user
    def get_balance(self, id_user):
        balance = self.model.retrieve_balance(id_user)
        return balance[0] if balance else 0
    # update the balance of the user
    
    def update_balance(self, id_user, amount):
        self.model.add_balance(id_user, amount)
        print("Solde mis à jour")
    
    def transfer(self, id_user, receiver_id, amount):
        sender_balance = self.model.retrieve_balance(id_user)
        if sender_balance[0] < amount:
            print("Solde insuffisant pour effectuer le virement.")
            return False
        else:
            self.model.add_balance(id_user, -amount)  
            self.model.add_balance(receiver_id, amount)  
            print("Virement effectué avec succès.")
            return True