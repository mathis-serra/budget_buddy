from databases.database import Database

class SqlManager(Database):
    def __init__(self):
        Database.__init__(self)
        
    def retreview_email(self):
        sql = "SELECT email FROM user"
        self.fetch_all(sql, ())
        
    def retreview_password(self):
        sql = "SELECT password FROM user"
        self.fetch_all(sql, ())
    
    
    
    
    
    
    