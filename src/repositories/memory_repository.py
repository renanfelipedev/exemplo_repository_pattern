class MemoryClienteRepository:
    def __init__(self):
        self._clientes = []
    
    def salvar(self, cliente):
        """Salva um cliente em memória"""
        print("[Repositório em Memória]: Salvando cliente...")
        self._clientes.append(cliente)
        return cliente
    
    def listar(self):
        """Listar todos os clientes em memória"""
        print("[Repositório em Memória]: Listando clientes...")
        return self._clientes

if __name__ == "__main__":
    pass