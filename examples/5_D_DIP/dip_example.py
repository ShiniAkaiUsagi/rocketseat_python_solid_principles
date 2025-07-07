from abc import ABC, abstractmethod

# Bad: Da forma como está abaixo, cria-se uma codependência entre ClientService e NotificatorEmail
#      Isso faz com que a funcionalidade da classe fique comprometida - relação direta com a classe NotificatorEmail, não funcionaria para SMS

# import dos módulos de baixo nível


# módulo de alto nível, não deveria depender diretamente dos módulos de baixo nível!


class BadNotificatorEmail:
    def send_notification(self, message: str):
        print(f"Sending email: {message}")


class BadNotificatorSMS:
    def send_notification(self, message: str):
        print(f"Sending sms: {message}")


class BadClientService:
    # Aqui temos uma relação direta com a dependência de baixo nível do NotificatorEmail, travando a classe
    def __init__(self, notificator: BadNotificatorEmail) -> None:
        self.notificator = notificator

    def send(self, message: str) -> None:
        self.notificator.send_notification(message)


# Good:


# Criou-se uma interface para trabalharmos sem dependência direta,
#     trabalhamos então direto com a interface, obrigando que a classe deve conter o send_notification esperado!
class NotificatorInterface(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        pass


class GoodNotificatorEmail(NotificatorInterface):
    def send_notification(self, message: str):
        print(f"Sending email: {message}")


class GoodNotificatorSMS(NotificatorInterface):
    def send_notification(self, message: str):
        print(f"Sending sms: {message}")


class GoodClientService:
    def __init__(self, notificator: NotificatorInterface) -> None:
        self.notificator = notificator

    def send(self, message: str) -> None:
        self.notificator.send_notification(message)
