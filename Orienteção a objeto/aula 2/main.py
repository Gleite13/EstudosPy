from random import randint
class Pessoa:
    anoAtual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.anoAtual - self.idade)

    @classmethod # @classmethod é um método que instância e retorna a classe a qual ele pertence
    def porAnoNascimento(cls, nome, anoNascimento):
        idade = cls.anoAtual - anoNascimento
        return nome
    @staticmethod # Não utiliza o self
    def gera_id():
        rand = randint(10000, 19999)
        return rand





p1 = Pessoa('Luiz', 32)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())
