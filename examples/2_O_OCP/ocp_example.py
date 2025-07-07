# BAD: para adicionar um novo worker seria necessário alterar a classe

from abc import ABC, abstractmethod


class BadCompany:
    def do_work(self, worker: int) -> None:
        if worker == 1:
            print("Programmer creating code")
        elif worker == 2:
            print("Seller selling the product")
        elif worker == 3:
            print("Human Resources hiring new people")
        # Adicionei manualmente mais um worker (4 - Dev)
        elif worker == 4:
            print("Dev raising bugs for production")
        else:
            print("Error, no Worker")


print("\nBadCompany example:")
company = BadCompany()
company.do_work(4)

# Good: Cria-se classes para cada 'worker' do exemplo, a partir de uma interface para padronizar
#       e a lógica principal se mantem a mesma!


class WorkerInterface(ABC):
    @abstractmethod
    def make(self):
        pass


class Programmer(WorkerInterface):
    def make(self):
        print("Programmer creating code")


class Seller(WorkerInterface):
    def make(self):
        print("Seller selling the product")


class HumanResource(WorkerInterface):
    def make(self):
        print("Human Resources hiring new people")


class Dev(WorkerInterface):
    def make(self):
        print("Dev raising bugs for production")


class GoodCompany:
    # Fechando para modificação
    def do_work(self, worker: WorkerInterface) -> None:
        worker.make()


print("\nGoodCompany example:")
company = GoodCompany()
company.do_work(Programmer())

# ou ainda
obj = Dev()
company.do_work(obj)
