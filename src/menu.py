from src.database.sqlite_connection import SqliteConnection
from src.database.mariadb_connection import MariaDBConnection

from src.repositories.sqlite_repository import SqliteClienteRepository
from src.repositories.mariadb_repository import MariaDBClienteRepository
from src.repositories.memory_repository import MemoryClienteRepository
from src.repositories.csv_repository import CsvClienteRepository

from src.service import ClienteService

class Menu:
    def _selecionar_repositorio():
        print("=== Selecione o Repositório de Dados ===")
        print("[1] Memória")
        print("[2] SQLite")
        print("[3] MariaDB")
        print("[4] Arquivo CSV")
        opcao = input("Informe o repositório desejado [1-4]: ").strip()

        match opcao:
            case "2":
                print("\n[Iniciado com SQLite]")
                connection = SqliteConnection()
                return SqliteClienteRepository(connection)
            case "3":
                print("\n[Iniciado com MariaDB]")
                connection = MariaDBConnection()
                return MariaDBClienteRepository(connection)
            case "4":
                print("\n[Iniciado com CSV]")
                return CsvClienteRepository()
            case _:
                print("\n[Iniciado com Memória]")
                return MemoryClienteRepository()

    def show():
        repository = Menu._selecionar_repositorio()
        service = ClienteService(repository)

        while True:
            print("[1] Cadastrar cliente")
            print("[2] Listar clientes")
            print("[99] Trocar repositório")
            print("[0] Sair")
            option = input("Informe a operação desejada: ").strip()

            match option:
                case "1":
                    print("\nCadastro de Cliente")
                    try:
                        name = input("Nome: ")
                        cpf = input("CPF: ")
                        email = input("E-mail: ")

                        cliente = service.cadastrar(name, cpf, email)

                        print(f"\nCliente cadastrado com sucesso: {cliente.to_dict()}")
                    except ValueError as e:
                        print(f"\n[Erro]: {e}")

                case "2":
                    try:
                        clientes = service.listar()

                        print("\n" + "=" * 65)
                        print(f"{'#':<4} | {'NOME':<22} | {'CPF':<15} | {'E-MAIL'}")
                        print("-" * 65)

                        for i, cliente in enumerate(clientes, start=1):
                            print(f"{i:<4} | {cliente.name:<22} | {cliente.cpf:<15} | {cliente.email}")

                        print("=" * 65)
                        print(f"Total: {len(clientes)} cliente(s) cadastrado(s).\n")

                    except ValueError as e:
                        print(f"\n[ERRO]: {e}\n")

                case "99":
                    print("\n--- Troca de Repositório ---")
                    repository = Menu._selecionar_repositorio()
                    service = ClienteService(repository)
                    print()

                case "0":
                    print("Até mais..")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    pass