# BAD: classe possui responsabilidade de conexão, verificação e cadastro, se eu mexo em uma, posso impactar as demais.


class BadProcess:
    def handle(self, username: str, password: str) -> None:
        if isinstance(username, str) and isinstance(password, str):
            print("Acesso ao banco de dados...")
            print("Verificando se usuário não possui registro...")
            print("Cadastro realizado com sucesso...")
        else:
            raise Exception("Dados inválidos")


# GOOD: Para qualquer ação nesse fluxo, agora posso alterar a própria função sem modificar o handle principal.


class GoodProcess:
    def handle(self, username: str, password: str) -> None:
        if self.__verify_input_data(username, password):
            self.__verify_input_in_database(username)
            self.__insert_new_user(username, password)
        else:
            self.__raise_error("Dados inválidos")

    def __verify_input_data(self, username: str, password: str) -> bool:
        return isinstance(username, str) and isinstance(password, str)

    def __verify_input_in_database(self, username: str) -> None:
        print("Acesso ao banco de dados...")
        print("Verificando existência do usuário")

    def __insert_new_user(self, username: str, password: str) -> None:
        print("Cadastro realizado com sucesso...")

    def __raise_error(self, message: str) -> Exception:
        raise Exception(message)


obj = GoodProcess().handle("user", "pass")
obj = GoodProcess().handle("user", 123)  # raise error, pass should be a string
