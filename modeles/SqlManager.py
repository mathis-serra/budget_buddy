# sql_manager.py

from modeles.Database import Database
from argon2 import PasswordHasher


class SqlManager(Database):
    def __init__(self):
        Database.__init__(self)
        
    # retrieve all the info from the user in the database
    def retrieve_user_info(self, email, password):
        sql = "SELECT firstname, name FROM user WHERE email = %s AND password = %s"
        user_info = self.fetch_one(sql, (email, password))
        return {'firstname': user_info[2], 'name': user_info[1]} if user_info else None
    
    # insert a new user in the database
    def insert_user(self, name, firstname, email, password):
        ph = PasswordHasher()
        hashed_password = ph.hash(password)
        sql = "INSERT INTO user (name, firstname, email, password, solde) VALUES (%s, %s, %s, %s, 0)"
        self.execute_sql(sql, (name, firstname, email, hashed_password))
    
    # verify the user in the database
    def verify_user(self, email, password):
        ph = PasswordHasher()
        sql = "SELECT * FROM user WHERE email = %s"
        user_info = self.fetch_one(sql, (email,))
        if user_info:
            print(user_info[3])

            if ph.verify(user_info[4], password):
                return {'firstname': user_info[2], 'name': user_info[1], 'id': user_info[0]}
        return None
 
    # add balance to the user
    def add_balance(self, id_user, amount):
        sql = "UPDATE user SET solde = solde + %s WHERE id_user = %s"
        self.execute_sql(sql, (amount, id_user))
    
    # retrieve the balance of the user
    def retrieve_balance(self, solde):
        sql = "SELECT solde FROM user WHERE id_user = %s"
        return self.fetch_one(sql, (solde,))

       
    
    def register_transaction(self, reason, type_transaction, amount):
        sql = "INSERT INTO transaction (reason, type_transaction, amount) VALUES (%s, %s, %s)"
        self.execute_sql(sql, (reason, type_transaction, amount))


    
    def retrieve_transactions(self, type_transaction):
        sql = "SELECT amount, reason FROM transaction WHERE type_transaction = %s"
        return self.fetch_all(sql, (type_transaction,))

