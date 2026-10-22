class Cliente:
    def __init__(self, name, cpf, email):
        self.name = name
        self.cpf = cpf
        self.email = email

    def __str__(self):
        return f"Nome: {self.name} | CPF: {self.cpf} | E-mail: {self.email}"

    def to_dict(self):
        return self.__dict__


if __name__ == "__main__":
    pass
