import tkinter as tk
from tkinter import font, messagebox
from controller.user_account import User_Account

class Account:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("MazeBank")
        self.root.geometry("430x600")
        self.root.configure(background='#f5f5f5')

        self.frame = tk.Frame(self.root, bg='#f5f5f5')
        self.frame.place(relx=0.5, rely=0.3, anchor='center')

        self.logo = tk.PhotoImage(file="logo.png").subsample(3)
        self.logo_label = tk.Label(self.frame, image=self.logo, bg='#f5f5f5')
        self.logo_label.pack(pady=5)

        self.custom_font = font.Font(family="Helvetica", size=20, weight="bold")
        self.title_label = tk.Label(self.frame, text="Bienvenue chez MazeBank", font=self.custom_font, bg='#f5f5f5', fg='black')
        self.title_label.pack(pady=2)

        self.create_account_info()
        User_Account.create_buttons()


        self.separator = tk.Frame(self.frame, height=2, width=400, bg='black')  # Utilisation de tk.Frame
        self.separator.pack(fill='x', pady=10)


    def create_account_info(self):
        self.account_title = tk.Label(self.frame, text="Compte individuel", font=('Helvetica', 16, 'bold'), bg='#f5f5f5', fg='black')
        self.account_title.pack(pady=5)

        self.account_number = tk.Label(self.frame, text="Numéro de compte : 12345678", font=('Arial', 12), bg='#f5f5f5', fg='black')
        self.account_number.pack(pady=5)

        self.account_holder = tk.Label(self.frame, text="Titulaire(s): Nom Prénom", font=('Arial', 16), bg='#f5f5f5', fg='black')
        self.account_holder.pack(pady=5, anchor='w')
    
    def create_button(self, text, command):
        button = tk.Button(self.frame, text=text, command=command, font=('Arial', 14), bg='#4CAF50', fg='red', padx=20, pady=10, bd=0, activebackground='#45a049', activeforeground='red')
        return button        

    def run(self):
        self.root.mainloop()


