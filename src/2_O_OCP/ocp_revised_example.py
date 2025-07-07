"""
OPEN CLOSED PRINCIPLE

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para
verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no código que, conforme a clínica adiciona exames,
deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle).
Utilizando do conceito do OCP, crie uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo
tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.

"""

from abc import ABC, abstractmethod


class ExameInterface(ABC):
    @abstractmethod
    def verifica_condicoes(self, exame):
        pass


class ExameSangue(ExameInterface):
    def verifica_condicoes(self, condicao):
        if not condicao:
            print("Exame de Sangue reprovado")
            return False
        print("Exame de sangue aprovado")
        return True


class ExameRaioX(ExameInterface):
    def verifica_condicoes(self, condicao: int):
        if not condicao:
            print("Exame de raio x reprovado")
            return False
        print("Exame de raio x aprovado")
        return True


class AprovaExame:
    def __init__(self, tipo_exame: ExameInterface) -> None:
        self.tipo_exame = tipo_exame

    def aprovar_solicitacao_exame(self, exame):
        self.tipo_exame.verifica_condicoes(exame)


exame_sangue = ExameSangue()
exame_raio_x = ExameRaioX()

aprovador_sangue = AprovaExame(exame_sangue)
condicao = True
aprovador_sangue.aprovar_solicitacao_exame(condicao)

aprovador_raio_x = AprovaExame(exame_raio_x)
condicao = False
aprovador_raio_x.aprovar_solicitacao_exame(condicao)
