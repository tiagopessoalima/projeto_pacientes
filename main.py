# api.py
from fastapi import FastAPI, HTTPException
from models.paciente import Paciente
from tree.arvore_binaria import ArvorePacientes

app = FastAPI(title="Triagem Hospitalar com Árvore Binária")

# Instância global da árvore (simula banco de dados em memória)
arvore = ArvorePacientes()

@app.post("/pacientes", status_code=201)
def inserir_paciente(nome: str, idade: int, gravidade: int):
    """Endpoint para inserir um novo paciente."""
    if not (0 <= gravidade <= 10):
        raise HTTPException(status_code=400, detail="Gravidade deve ser entre 0 e 10")
    if idade < 0 or idade > 120:
        raise HTTPException(status_code=400, detail="Idade inválida")

    paciente = Paciente(nome, idade, gravidade)
    arvore.inserir(paciente)
    return {"mensagem": "Paciente inserido", "paciente": paciente.__repr__()}

@app.get("/pacientes")
def listar_pacientes():
    """Retorna todos os pacientes ordenados por gravidade (crescente)."""
    resultado = []
    def coletar(no):
        if no:
            coletar(no.esquerda)
            for p in no.pacientes:
                resultado.append({
                    "nome": p.nome,
                    "idade": p.idade,
                    "gravidade": p.gravidade
                })
            coletar(no.direita)
    coletar(arvore.raiz)
    return {"pacientes": resultado}

@app.get("/pacientes/gravidade/{gravidade}")
def buscar_por_gravidade(gravidade: int):
    """Busca pacientes com uma determinada gravidade."""
    if not (0 <= gravidade <= 10):
        raise HTTPException(status_code=400, detail="Gravidade deve ser entre 0 e 10")
    pacientes = arvore.buscar_por_gravidade(gravidade)
    if pacientes is None:
        return {"gravidade": gravidade, "pacientes": []}
    return {
        "gravidade": gravidade,
        "pacientes": [
            {"nome": p.nome, "idade": p.idade, "gravidade": p.gravidade}
            for p in pacientes
        ]
    }