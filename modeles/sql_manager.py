# sql_manager.py

from modeles.database import Database

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
        sql = "INSERT INTO user (name, firstname, email, password) VALUES (%s, %s, %s, %s)"
        self.execute_sql(sql, (name, firstname, email, password))
    
    def verify_user(self, email, password):
        sql = "SELECT * FROM user WHERE email = %s AND password = %s"
        user_info = self.fetch_one(sql, (email, password))
        return {'firstname': user_info[2], 'name': user_info[1]} if user_info else None
