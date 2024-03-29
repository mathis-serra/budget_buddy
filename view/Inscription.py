import tkinter as tk
from tkinter import font 
# Label, Button
from view.placeholderEntry import PlaceholderEntry 
from view.connection import Connection

class Inscription(PlaceholderEntry):
    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.root.title("MazeBank - Inscription")
        self.root.geometry("430x600")
        self.root.configure(background='#f5f5f5')
        self.create_widget_register()

        
    def create_widget_register(self):
        self.custom_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.title_label = tk.Label(self.root, text="MAZE BANK", font=self.custom_font, bg='#f5f5f5', fg='black')
        self.title_label.pack()

        self.inscription_title = tk.Label(self.root, text="Inscription", font=('Arial', 18, 'bold'), bg='#f5f5f5', fg='#DB0000')
        self.inscription_title.pack(pady=10)

        self.nom_entry = PlaceholderEntry(self.root, "Nom", font=('Arial', 12), bg='white', fg='black')
        self.nom_entry.pack(pady=5)

        self.prenom_entry = PlaceholderEntry(self.root, "Prénom", font=('Arial', 12), bg='white', fg='black')
        self.prenom_entry.pack(pady=5)

        self.email_entry = PlaceholderEntry(self.root, "Email", font=('Arial', 12), bg='white', fg='black')
        self.email_entry.pack(pady=5)

        self.mdp_entry = PlaceholderEntry(self.root, "Mot de passe", font=('Arial', 12), bg='white', fg='black')
        self.mdp_entry.pack(pady=5)

        self.inscription_button = tk.Button(self.root, text="S'inscrire", command=self.inscrire, font=('Arial', 14), bg='white', fg='#DB0000', padx=20, pady=10, bd=0, activebackground='#FF5733', activeforeground='white')
        self.inscription_button.pack(pady=10)

        self.connection_button = tk.Button(self.root, text="Se connecter", command=self.go_to_connection, font=('Arial', 14), bg='#DB0000', fg='#DB0000', padx=20, pady=10, bd=0, activebackground='#FF5733', activeforeground='white')
        self.connection_button.pack(pady=10)

    def inscrire(self):
        pass

    def go_to_connection(self):
        self.root.destroy()
        app = Connection()
        app.run_connection()
    
    def run_register(self):
        self.root.mainloop()

# # if __name__ == "__main__":
#     app = Inscription()
#     app.run_register()
