import pygame, re
from database.sql_manager import SqlManager
from tool_graph.element import Elements

class Connection(SqlManager, Elements):
    def __init__(self):
        super().__init__()
        self.email_text = ""
        self.password_text = ""
        self.active_field = {'email':'', 'password':''}
        self.clock = pygame.time.Clock()
        self.error_timer = 0
        self.error_duration = 1000

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
        if self.error_email:
            self.solid_rect_radius(self.red,620,20,360,55,8)
            self.light_rect(self.black,620,20,360,55,2)
            self.text_align(16, self.error_email, self.black, 796, 45)
            self.error_timer += self.clock.tick()
            if self.error_timer >= self.error_duration:
                self.error_email = ""
                self.error_timer = 0
                
        elif self.error_password:
            self.solid_rect_radius(self.red,620,20,360,55,8)
            self.light_rect(self.black,620,20,360,55,2)
            self.text_align(16, self.error_password, self.black, 796, 45)
            self.error_timer += self.clock.tick()
            if self.error_timer >= self.error_duration:
                self.error_password = ""
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
    
    def verify_password(self, password_input):
        if password_input:
            # Vérification de la longueur minimale
            if len(password_input) < 10:
                self.error_password = "Mot de passe trop court"
                return False  # Mot de passe trop court
            
            # Vérification de la présence de majuscules, minuscules, chiffres et caractères spéciaux
            if not re.search(r"[A-Z]", password_input):
                self.error_password = "Le mot de passe doit contenir une majuscule"
                return False  # Pas de majuscule
            if not re.search(r"[a-z]", password_input):
                self.error_password = "Le mot de passe doit contenir une minuscule"
                return False  # Pas de minuscule
            if not re.search(r"\d", password_input):
                self.error_password = "Le mot de passe doit contenir au moin un chiffre"
                return False  # Pas de chiffre
            if not re.search(r"[!@#$%^&*()-_+=]", password_input):
                self.error_password = "Un caractère spécial requis"
                return False  # Pas de caractère spécial

            return True  # Mot de passe valide
        self.error_password = "Veuillez saisir votre mot de passe" 
        return False  # Mot de passe vide ou None
    
    def button_click(self):
        pass
        
    
    def connect(self):
        pass
