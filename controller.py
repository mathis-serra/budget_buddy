from sql_manager import SqlManager


class Controller:
    def __init__(self, view):
        self.view = view
        self.model = SqlManager()

    def register_user(self, name, firstname, email, password):
        try:
            # Insérer l'utilisateur dans la base de données via le modèle
            self.model.insert_user(name, firstname, email, password)
            print("Utilisateur enregistré avec succès")
        except Exception as e:
            print("Erreur lors de l'enregistrement de l'utilisateur:", e)