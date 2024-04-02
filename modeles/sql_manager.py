# sql_manager.py

from modeles.database import Database
from argon2 import PasswordHasher
import bcrypt

class SqlManager(Database):
    def __init__(self):
        Database.__init__(self)
        
    def retrieve_email(self):
        sql = "SELECT email FROM user"
        return self.fetch_all(sql, ())
        
    def retrieve_password(self):
        sql = "SELECT password FROM user"
        return self.fetch_all(sql, ())
    
    def retrieve_user_info(self, email, password):
        sql = "SELECT firstname, name FROM user WHERE email = %s AND password = %s"
        user_info = self.fetch_one(sql, (email, password))
        return {'firstname': user_info[2], 'name': user_info[1]} if user_info else None
    
    def insert_user(self, name, firstname, email, password):
        ph = PasswordHasher()
        hashed_password = ph.hash(password)
        sql = "INSERT INTO user (name, firstname, email, password, solde) VALUES (%s, %s, %s, %s, 0)"
        self.execute_sql(sql, (name, firstname, email, hashed_password))
    
    def verify_user(self, email, password):
        ph = PasswordHasher()
        sql = "SELECT * FROM user WHERE email = %s"
        user_info = self.fetch_one(sql, (email,))
        if user_info:
            print(user_info[3])

            if ph.verify(user_info[4], password):
                return {'firstname': user_info[2], 'name': user_info[1], 'id': user_info[0]}
        return None


    
    
    def add_balance(self, id_user, amount):
        sql = "UPDATE user SET solde = solde + %s WHERE id_user = %s"
        self.execute_sql(sql, (amount, id_user))
        
    def retrieve_balance(self, solde):
        sql = "SELECT solde FROM user WHERE id_user = %s"
        return self.fetch_one(sql, (solde,))

