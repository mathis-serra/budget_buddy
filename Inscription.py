import tkinter as tk
from tkinter import font
from connection import Connection
from controller import Controller

class Inscription:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        # Initialisation de l'interface graphique
        self.initialize_ui()

    def initialize_ui(self):
        self.root.title("MazeBank - Inscription")
        self.root.geometry("430x600")
        self.root.configure(background='#f5f5f5')

        # Autres éléments d'interface graphique (labels, entry, buttons) ...

    def register(self):
        # Récupérer les valeurs des champs d'entrée
        firstname = self.prenom_entry.get()
        name = self.nom_entry.get()
        email = self.email_entry.get()
        password = self.mdp_entry.get()

        # Appeler la méthode du contrôleur pour enregistrer l'utilisateur
        self.controller.register_user(name, firstname, email, password)

    def go_to_connection(self):
        self.root.destroy()  # Fermer la fenêtre d'inscription
        app = Connection()    # Ouvrir la fenêtre de connexion
        app.create_widgets()
        app.run()

class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = 'grey'
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.focused)
        self.bind("<FocusOut>", self.focus_out)
        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def focused(self, event):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def focus_out(self, event):
        if not self.get():
            self.put_placeholder()
            self['fg'] = self.placeholder_color

if __name__ == "__main__":
    root = tk.Tk()
    controller = Controller()
    app = Inscription(root, controller)
    root.mainloop()
