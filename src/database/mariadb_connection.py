try:
    import pymysql
except ImportError:
    pymysql = None


class MariaDBConnection:
    def __init__(self, host="localhost", user="root", password="123123", database="projeto", port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

    def connect(self, use_database=True):
        """Retorna uma nova conexão com o MariaDB/MySQL. 
        Se use_database=False, conecta ao servidor sem selecionar um banco específico."""
        if pymysql is None:
            raise ImportError(
                "Driver 'pymysql' não encontrado. Instale com: pip install pymysql"
            )

        kwargs = {
            "host": self.host,
            "user": self.user,
            "password": self.password,
            "port": self.port,
        }
        if use_database and self.database:
            kwargs["database"] = self.database

        return pymysql.connect(**kwargs)


if __name__ == "__main__":
    pass
