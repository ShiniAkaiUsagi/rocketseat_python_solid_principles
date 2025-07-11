"""
SINGLE RESPONSABILITY PRINCIPLE

Note que nessa classe, temos várias ações e responsabilidades. O que torna a manutenção, usabilidade e até a performance ruins.

Seguindo o conceito do Princípio da Responsabilidade única, organize essa classe e, se necessário, crie outras
classes com suas devidas responsabilidades.

"""


class ApiClient:
    def connect_api():
        pass


class TaskHandler:
    def create_task():
        pass

    def update_task():
        pass

    def remove_task():
        pass


class Notificator:
    def send_notification():
        pass


class ReportHandler:
    def generate_report():
        pass

    def send_report():
        pass
