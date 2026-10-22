from src.database.sqlite_connection import SqliteConnection
from src.entities.cliente import Cliente

class SqliteClienteRepository:
    def __init__(self, connection: SqliteConnection):
        self.connection = connection
        self._criar_tabela()

    def _criar_tabela(self):
        """Cria a tabela de clientes se ela não existir."""
        with self.connection.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    cpf TEXT UNIQUE NOT NULL,
                    email TEXT NOT NULL
                )
                """
            )
            conn.commit()

    def salvar(self, cliente):
        """Salva um cliente no banco de dados SQLite."""
        print("[Repositório SQLite]: Salvando cliente no banco de dados...")
        with self.connection.connect() as connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO clientes (name, cpf, email) VALUES (?, ?, ?)",
                (cliente.name, cliente.cpf, cliente.email)
            )
            connection.commit()
        return cliente

    def listar(self):
        """Recupera todos os clientes do banco de dados e retorna objetos Cliente."""
        print("[Repositório SQLite]: Listando clientes do banco de dados...")
        with self.connection.connect() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT name, cpf, email FROM clientes")
            linhas = cursor.fetchall()

        return [Cliente(name=row[0], cpf=row[1], email=row[2]) for row in linhas]


if __name__ == "__main__":
    pass
