from src.database.mariadb_connection import MariaDBConnection
from src.entities.cliente import Cliente


class MariaDBClienteRepository:
    def __init__(self, connection: MariaDBConnection):
        self.connection = connection
        self._criar_banco()
        self._criar_tabela()

    def _criar_banco(self):
        """Cria o banco de dados se ele não existir no MariaDB."""
        with self.connection.connect(use_database=False) as conn:
            cursor = conn.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{self.connection.database}`")
            conn.commit()

    def _criar_tabela(self):
        """Cria a tabela de clientes se ela não existir no MariaDB."""
        with self.connection.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS clientes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    cpf VARCHAR(14) UNIQUE NOT NULL,
                    email VARCHAR(255) NOT NULL
                )
                """
            )
            conn.commit()

    def salvar(self, cliente):
        """Salva um cliente no banco de dados MariaDB."""
        print("[Repositório MariaDB]: Salvando cliente no banco de dados...")
        with self.connection.connect() as connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO clientes (name, cpf, email) VALUES (%s, %s, %s)",
                (cliente.name, cliente.cpf, cliente.email),
            )
            connection.commit()
        return cliente

    def listar(self):
        """Recupera todos os clientes do banco de dados MariaDB e retorna objetos Cliente."""
        print("[Repositório MariaDB]: Listando clientes do banco de dados...")
        with self.connection.connect() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT name, cpf, email FROM clientes")
            linhas = cursor.fetchall()

        return [Cliente(name=row[0], cpf=row[1], email=row[2]) for row in linhas]


# Alias caso queira chamar de MySQLClienteRepository
MySQLClienteRepository = MariaDBClienteRepository

if __name__ == "__main__":
    pass
