import tkinter as tk
from tkinter import font
from interface import Interface
from tkinter import messagebox


class Connexion:
    def __init__(self, root):
        self.root = root
        self.root.title("MazeBank - Inscription")
        self.root.geometry("430x600") 
        self.root.configure(background='#f5f5f5')

        # Redimensionnement du logo
        self.logo = tk.PhotoImage(file="logo.png").subsample(2)  
        self.logo_label = tk.Label(self.root, image=self.logo, bg='#f5f5f5')
        self.logo_label.pack(pady=20)

        self.custom_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.title_label = tk.Label(self.root, text="MAZE BANK", font=self.custom_font, bg='#f5f5f5', fg='black')
        self.title_label.pack()

        self.connexion_title = tk.Label(self.root, text="Connexion", font=('Arial', 18, 'bold'), bg='#f5f5f5', fg='#DB0000')
        self.connexion_title.pack(pady=10)

        self.email_entry = PlaceholderEntry(self.root, "Email", font=('Arial', 12), bg='white', fg='black')
        self.email_entry.pack(pady=5)

        self.mdp_entry = PlaceholderEntry(self.root, "Mot de passe", font=('Arial', 12), bg='white', fg='black')
        self.mdp_entry.pack(pady=5)

        self.connexion_button = tk.Button(self.root, text="Se connecter", command=self.connecter, font=('Arial', 14), bg='red', fg='red', padx=20, pady=10, bd=0, activebackground='#FF5733', activeforeground='red')
        self.connexion_button.pack(pady=10)

    def connecter(self):
        email = self.email_entry.get()
        password = self.mdp_entry.get() 
        if self.verifier_connexion(email, password):
                self.root.destroy()  # Détruire la fenêtre de connexion
                root_interface = tk.Tk()  # Créer une nouvelle instance de Tk
                app_interface = Interface(root_interface)  # Créer une instance de Menu dans la même instance de Tk
                root_interface.mainloop()

    def verifier_connexion(self, email, password):
        # Cette méthode devrait vérifier les informations de connexion.
        # Ici, nous simulerons une vérification réussie si l'email est "test@test.com" et le mot de passe est "password".
        if email == "test@test.com" and password == "password":
            return True
        else:
            # Si les informations de connexion ne sont pas valides, vous pouvez afficher un message d'erreur.
            messagebox.showerror("Erreur de connexion", "Email ou mot de passe incorrect.")
            return False


class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="", color='grey', *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)
        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def on_focus_in(self, event):
        if self['fg'] == self.placeholder_color:
            self.delete(0, tk.END)
            self['fg'] = self.default_fg_color

    def on_focus_out(self, event):
        if not self.get():
            self.put_placeholder()


if __name__ == "__main__":
    root = tk.Tk()
    app = Connexion(root)
    root.mainloop()
