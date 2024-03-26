import pygame
from database.sql_manager import SqlManager
from 

class Connection(SqlManager):
    def __init__(self):
        super().__init__()
        self.email_text = ""
        self.password_text = ""
        self.active_field = {'email':'', 'password':''}

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if self.active_field == "email":
                    self.email_text = self.email_text[:-1]
                elif self.active_field == "password":
                    self.password_text = self.password_text[:-1]
            elif event.key == pygame.K_RETURN:
                if self.active_field == "email":
                    print("Email saisi :", self.email_text)
                    self.email_text = ""
                elif self.active_field == "password":
                    print("Mot de passe saisi :", self.password_text)
                    self.password_text = ""
            else:
                if self.active_field == "email":
                    self.email_text += event.unicode
                elif self.active_field == "password":
                    self.password_text += event.unicode
                    
    def draw_error_message_login(self):
        """
        Draw error message for login.
        """
        if self.error_message_login:
            self.solid_rect_radius(self.light_grey,620,20,360,55,8)
            self.light_rect(self.black,620,20,360,55,2)
            self.text_align(16, self.error_message_login, self.pur_red, 796, 45)
            self.error_timer += self.clock.tick()
            if self.error_timer >= self.error_duration:
                self.error_message_login = None
                self.error_timer = 0
                
    def verify_email(self, email_input):
        if email_input:
            # Vérification de la présence d'un "@" et d'au moins un "."
            if "@" in email_input and "." in email_input:
                # Vérification de l'unicité de l'email
                if email_input == self.retreview_email():
                    return True  # Email valide et unique
                else:
                    self.error_email = "Vous n'avez pas de compte avec cette email"
                    return False  # Email valide mais non unique
            else:
                self.error_email = "Je ne comprend pas l'email sasie, veuillez réessayer"
                return False  # Email invalide (manque "@" ou ".")
        else:
            self.error_email = "Veuillez saisir un email"
            return False  # Email vide
    
    def verify_password(self, input_password):
        pass
    
    def button_click(self):
        pass
        
    
    def connect(self):
        pass
