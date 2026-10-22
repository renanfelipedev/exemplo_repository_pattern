import os
import sqlite3

class SqliteConnection:
    def __init__(self, db_path="dados/database.sqlite"):
        self.db_path = db_path

        dir_name = os.path.dirname(self.db_path)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name, exist_ok=True)

    def connect(self):
        """Retorna uma nova conexão com o banco de dados SQLite."""
        return sqlite3.connect(self.db_path)


if __name__ == "__main__":
    pass