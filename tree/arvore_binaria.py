from models.paciente import Paciente

class No:
    def __init__(self, gravidade: int, paciente: Paciente):
        self.gravidade = gravidade
        self.pacientes = [paciente]   # lista para pacientes com mesma gravidade
        self.esquerda = None
        self.direita = None

class ArvorePacientes:
    def __init__(self):
        self.raiz = None

    def inserir(self, paciente: Paciente):
        """Insere um paciente na árvore baseado na gravidade."""
        if self.raiz is None:
            self.raiz = No(paciente.gravidade, paciente)
        else:
            self._inserir_rec(self.raiz, paciente)

    def _inserir_rec(self, no: No, paciente: Paciente):
        if paciente.gravidade < no.gravidade:
            if no.esquerda is None:
                no.esquerda = No(paciente.gravidade, paciente)
            else:
                self._inserir_rec(no.esquerda, paciente)
        elif paciente.gravidade > no.gravidade:
            if no.direita is None:
                no.direita = No(paciente.gravidade, paciente)
            else:
                self._inserir_rec(no.direita, paciente)
        else:  # gravidade igual
            no.pacientes.append(paciente)

    def em_ordem(self):
        """Percorre em ordem (crescente por gravidade)."""
        self._em_ordem_rec(self.raiz)

    def _em_ordem_rec(self, no: No):
        if no:
            self._em_ordem_rec(no.esquerda)
            for p in no.pacientes:
                print(p)
            self._em_ordem_rec(no.direita)

    def buscar_por_gravidade(self, gravidade: int):
        """Retorna lista de pacientes com determinada gravidade."""
        return self._buscar_rec(self.raiz, gravidade)

    def _buscar_rec(self, no: No, gravidade: int):
        if no is None:
            return None
        if gravidade < no.gravidade:
            return self._buscar_rec(no.esquerda, gravidade)
        elif gravidade > no.gravidade:
            return self._buscar_rec(no.direita, gravidade)
        else:
            return no.pacientes