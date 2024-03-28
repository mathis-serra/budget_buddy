import tkinter as tk
from tkinter import font
from connection import Connection 

class Inscription:
    def __init__(self):
        self.root = root
        self.root.title("MazeBank - Inscription")
        self.root.geometry("430x600")  # Nouvelles dimensions de la fenêtre
        self.root.configure(background='#f5f5f5')

        # Redimensionnement du logo
        self.logo = tk.PhotoImage(file="logo.png").subsample(2)  # Changer le facteur de sous-échantillonnage selon votre besoin
        self.logo_label = tk.Label(self.root, image=self.logo, bg='#f5f5f5')
        self.logo_label.pack(pady=20)

        self.custom_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.title_label = tk.Label(self.root, text="MAZE BANK", font=self.custom_font, bg='#f5f5f5', fg='black')
        self.title_label.pack()

        # Titre "Inscription" en rouge
        self.inscription_title = tk.Label(self.root, text="Inscription", font=('Arial', 18, 'bold'), bg='#f5f5f5', fg='#DB0000')
        self.inscription_title.pack(pady=10)

        # Boîtes à remplir avec placeholder
        self.nom_entry = PlaceholderEntry(self.root, "Nom", font=('Arial', 12), bg='white', fg='black')
        self.nom_entry.pack(pady=5)

        self.prenom_entry = PlaceholderEntry(self.root, "Prénom", font=('Arial', 12), bg='white', fg='black')
        self.prenom_entry.pack(pady=5)

        self.email_entry = PlaceholderEntry(self.root, "Email", font=('Arial', 12), bg='white', fg='black')
        self.email_entry.pack(pady=5)

        self.mdp_entry = PlaceholderEntry(self.root, "Mot de passe", font=('Arial', 12), bg='white', fg='black')
        self.mdp_entry.pack(pady=5)

        # Boutons "S'inscrire" et "Se connecter"
        self.inscription_button = tk.Button(self.root, text="S'inscrire", command=self.inscrire, font=('Arial', 14), bg='white', fg='#DB0000', padx=20, pady=10, bd=0, activebackground='#FF5733', activeforeground='white')
        self.inscription_button.pack(pady=10)

        self.connection_button = tk.Button(self.root, text="Se connecter", command=self.go_to_connection, font=('Arial', 14), bg='#DB0000', fg='#DB0000', padx=20, pady=10, bd=0, activebackground='#FF5733', activeforeground='white')
        self.connection_button.pack(pady=10)

    def inscrire(self):
        # Fonction pour traiter l'inscription (à implémenter plus tard)
        pass

    def go_to_connection(self):
        self.root.destroy()  # Ferme la fenêtre du menu principal
        app = Connection()
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
    app = Inscription(root)
    root.mainloop()
