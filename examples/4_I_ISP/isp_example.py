# Exemplo em que trabalhamos com vários arquivos: pdf / txt / excel
# excel: def calcular() | txt: def formatar() | pdf: def visualizar()


# Bad: Classe genérica que atende a diversos documentos, poderia usar funções do excel no pdf por engano, por exemplo
#    Dessa forma, sou obrigado/forçado a implementar métodos que não quero/preciso utilizar
from abc import ABC, abstractmethod


class Document(ABC):

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def view(self):
        pass

    @abstractmethod
    def format(self):
        pass

    @abstractmethod
    def calculate(self):
        pass


# Exemplo de uso (descomente):
# class PDF(Document):
#     def load(self):
#         print("load in pdf")

#     def view(self):
#         print("View infos")

# document1 = PDF()
# # > Retornaria erro, pois a interface pede mais métodos que não são para PDF

# Good: Segregando a interface em partes menores e específicas
# #     assim conseguimos trabalhar com a abstração somente do que cada classe de arquivo precisa


class DocumentPDF(ABC):  # ISP
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def view(self):
        pass


class DocumentTXT(ABC):  # ISP
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def format(self):
        pass


class DocumentXLSX(ABC):  # ISP
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def calculate(self):
        pass


# Agora temos uma classe PDF que não me força a ter métodos que não utilizarei
class PDF(DocumentPDF):
    def load(self):
        print("Loading PDF")

    def view(self):
        print("Viewing PDF")


pdf = PDF()
pdf.load()
pdf.view()
