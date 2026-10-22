from src.entities.cliente import Cliente

class ClienteService:
    def __init__(self, repository):
        self.repository = repository

    def validar_dados(self, name, cpf, email):
        if not name:
            raise ValueError("O nome é obrigatório.")
        if not cpf:
            raise ValueError("O CPF é obrigatório.")
        if not email:
            raise ValueError("O E-mail é obrigatório.")
        if len(cpf) != 11:
            raise ValueError("O CPF deve ter 11 dígitos numéricos. ")
        
    def cadastrar(self, name: str, cpf: str, email: str):
        self.validar_dados(name, cpf, email)

        cliente = Cliente(name, cpf, email)
        
        return self.repository.salvar(cliente)
    
    def listar(self):
        clientes = self.repository.listar()

        if not clientes:
            raise ValueError("Nenhum cliente cadastrado.")

        return clientes
        


if __name__ == "__main__":
    pass
