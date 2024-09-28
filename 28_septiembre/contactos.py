import mysql.connector

class Database:
    def __init__(self):
        self.connexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "admin",
            database = "contactosdb"
        )

        self.cursor = self.connexion.cursor()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.connexion.commit()

    def fetch_query(self, query, params= None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()