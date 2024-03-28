import tkinter as tk
from tkinter import font
# from connection import Connection
from controller import Controller

class Inscription:
    def __init__(self, root):
        self.root = root
        # self.controller = controller

        
        self.initialize_ui()

    def initialize_ui(self):
        self.root.title("MazeBank - Inscription")
        self.root.geometry("430x600")
        self.root.configure(background='#f5f5f5')

        

    def register(self):
        
        firstname = self.prenom_entry.get()
        name = self.nom_entry.get()
        email = self.email_entry.get()
        password = self.mdp_entry.get()

        
        self.controller.register_user(name, firstname, email, password)

    # def go_to_connection(self):
    #     self.root.destroy()  
    #     app = Connection()    
    #     app.create_widgets()
    #     app.run()

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
    Controller = Controller(app)
    root.mainloop()
