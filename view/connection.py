import tkinter as tk
from tkinter import font, Label, Button, messagebox
from view.placeholderEntry import PlaceholderEntry
from control.controller import Controller
from view.Account import Menu

class Connection:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        self.root.title("MazeBank - Connexion")
        self.root.geometry("430x800")
        self.root.configure(background='#f5f5f5')

        # Logo et titre
        self.logo = tk.PhotoImage(file="assets/logo.png").subsample(2)
        self.logo_label = tk.Label(self.root, image=self.logo, bg='#f5f5f5')
        self.logo_label.pack(pady=20)
        self.title_label = tk.Label(self.root, text="MAZE BANK", font=('Helvetica', 24, 'bold'), bg='#f5f5f5', fg='black')
        self.title_label.pack()

        # Zone de connexion
        self.connexion_title = Label(self.root, text="Connexion", font=('Arial', 18, 'bold'), bg='#f5f5f5', fg='#DB0000')
        self.connexion_title.pack(pady=10)
        self.email_entry = PlaceholderEntry(self.root, "Email", font=('Arial', 12), bg='white', fg='black')
        self.email_entry.pack(pady=5)
        self.password_entry = PlaceholderEntry(self.root, "Mot de passe", font=('Arial', 12), bg='white', fg='black', show='*')
        self.password_entry.pack(pady=5)
        self.connexion_button = Button(self.root, text="Se connecter", command=self.login, font=('Arial', 14), bg='red', fg='white', padx=20, pady=10, bd=0, activebackground='#FF5733', activeforeground='white')
        self.connexion_button.pack(pady=10)
        
    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        user_info = self.controller.login_user(email, password)
        if user_info:
            self.root.destroy()
            root = tk.Tk()
            app = Menu(root, user_info)
            root.mainloop()
        else:
            messagebox.showerror("Erreur de connexion", "Adresse e-mail ou mot de passe incorrect.")

def run_connection(self):
    root = tk.Tk()
    controller = Controller(None)  
    connection = Connection(root, controller)
    connection.run_connection()


