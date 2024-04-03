import mysql.connector

class Database:
    
    # Connect to the database
    def __init__(self):
        self.base = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dominique59",
            database="maze_bank",
        )
        self.cursor = self.base.cursor()
    # Execute the query
    def execute_sql(self, query, params):
        self.cursor.execute(query, params or ())
        self.base.commit()

    # Fetch all the results
    def fetch_all(self, query, params):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()
    

    # Fetch one result
    def fetch_one(self, query, params):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchone()

    # Close the connection
    def closing_connection(self):
        self.base.close()
