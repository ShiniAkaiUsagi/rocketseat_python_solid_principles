# Bad:


class Animal:
    def comer(self):
        print("O Animal está comendo")

    def andar(self):
        print("O Animal está andando na selva")


class BadFelino(Animal):
    def lamber(self):
        print("O Felino está lambendo seu pelo")


print("\nBad example logs")

animal = Animal()
felino = BadFelino()

animal.comer()
felino.comer()


# Good: Atenção a cadeia de heranças, reaproveitamos métodos mais genéricos da classe mãe.


class GoodFelino(Animal):
    def lamber(self):
        print("O Felino está lambendo seu pelo")

    def comer(self):
        print("O felino come sua ração")


# mais um exemplo para ilustrar
class Leao(GoodFelino):
    def rugir(self):
        print("O leão está rugindo")


class Pessoa:
    def observa(self, animal: Animal):
        animal.comer()


print("\nGood example logs")
animal = Animal()
felino = GoodFelino()
leao = Leao()

leao.comer()
leao.rugir()

animal.comer()
felino.comer()

pessoa = Pessoa()
pessoa.observa(animal)
pessoa.observa(felino)
