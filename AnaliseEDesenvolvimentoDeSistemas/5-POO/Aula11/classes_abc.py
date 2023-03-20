from abc import ABC, abstractclassmethod


class Funcionario(ABC):
    @abstractclassmethod
    def t(self):
        pass


@property
@abstractclassmethod
def nome(self):
    return self.nome


class Vendedor(Funcionario):
    def salario(self):
        return "calculo 1"


class Estagiario(Funcionario):
    def salario(self):
        return "calculo 2"
