import csv
import os
from src.entities.cliente import Cliente


class CsvClienteRepository:
    def __init__(self, file_path="dados/clientes.csv"):
        self.file_path = file_path
        self._inicializar_arquivo()

    def _inicializar_arquivo(self):
        """Cria a pasta e o arquivo CSV com o cabeçalho se ainda não existirem."""
        dir_name = os.path.dirname(self.file_path)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name, exist_ok=True)

        if not os.path.exists(self.file_path):
            with open(self.file_path, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["name", "cpf", "email"])

    def salvar(self, cliente):
        """Salva um cliente no final do arquivo CSV."""
        print("[Repositório CSV]: Salvando cliente no arquivo CSV...")
        with open(self.file_path, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([cliente.name, cliente.cpf, cliente.email])
        return cliente

    def listar(self):
        """Lê os clientes do arquivo CSV e retorna uma lista de objetos Cliente."""
        print("[Repositório CSV]: Listando clientes do arquivo CSV...")
        if not os.path.exists(self.file_path):
            return []

        clientes = []
        with open(self.file_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            # Pula o cabeçalho ("name", "cpf", "email")
            next(reader, None)

            for row in reader:
                if row:  # Evita linhas em branco
                    cliente = Cliente(name=row[0], cpf=row[1], email=row[2])
                    clientes.append(cliente)

        return clientes


if __name__ == "__main__":
    pass
