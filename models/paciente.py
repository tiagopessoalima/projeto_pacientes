class Paciente:
    def __init__(self, nome: str, idade: int, gravidade: int):
        self.nome = nome
        self.idade = idade
        self.gravidade = gravidade

    def __repr__(self):
        return f"{self.nome} | Idade: {self.idade} | Gravidade: {self.gravidade}"