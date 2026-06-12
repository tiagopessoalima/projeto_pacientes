# 🏥 Triagem Hospitalar com Árvore Binária

Sistema de triagem hospitalar desenvolvido com **FastAPI** e **Árvore Binária de Busca (ABB)** para gerenciamento de pacientes conforme o nível de gravidade.

Este projeto demonstra a aplicação prática de estruturas de dados em um contexto de saúde, permitindo o armazenamento e a consulta eficiente de pacientes por prioridade de atendimento.

---

## 🚀 Funcionalidades

* Inserção de pacientes com:

  * Nome
  * Idade
  * Gravidade (0 a 10)
* Listagem de todos os pacientes em ordem crescente de gravidade
* Busca de pacientes por nível específico de gravidade
* Suporte a múltiplos pacientes com a mesma gravidade

---

## 🧠 Estrutura de Dados

A aplicação utiliza uma **Árvore Binária de Busca (ABB)** onde a chave de ordenação é o nível de gravidade do paciente.

### Estrutura dos nós

Cada nó da árvore contém:

```text
Nó
├── gravidade (chave)
├── pacientes (lista de pacientes)
├── esquerda
└── direita
```

### Complexidade média

| Operação          | Complexidade |
| ----------------- | ------------ |
| Inserção          | O(log n)     |
| Busca             | O(log n)     |
| Listagem ordenada | O(n)         |

---

## 🛠️ Tecnologias Utilizadas

* Python 3.10+
* FastAPI
* Uvicorn
* Pydantic

---

## 📦 Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/triagem-arvore-binaria.git
cd triagem-arvore-binaria
```

### 2. Instalar as dependências

```bash
pip install fastapi uvicorn
```

### 3. Executar a aplicação

```bash
uvicorn main:app --reload
```

---

## 📚 Documentação da API

Após iniciar o servidor, acesse:

| Tipo       | URL                                                        |
| ---------- | ---------------------------------------------------------- |
| Swagger UI | [http://localhost:8000/docs](http://localhost:8000/docs)   |
| ReDoc      | [http://localhost:8000/redoc](http://localhost:8000/redoc) |

---

## 📍 Endpoints

### Inserir paciente

**POST** `/pacientes`

#### Exemplo

```bash
curl -X POST "http://localhost:8000/pacientes?nome=Maria&idade=45&gravidade=7"
```

#### Resposta

```json
{
  "mensagem": "Paciente inserido",
  "paciente": "Maria | Idade: 45 | Gravidade: 7"
}
```

---

### Listar pacientes

**GET** `/pacientes`

#### Resposta

```json
{
  "pacientes": [
    {
      "nome": "João",
      "idade": 30,
      "gravidade": 2
    },
    {
      "nome": "Maria",
      "idade": 45,
      "gravidade": 7
    },
    {
      "nome": "Carlos",
      "idade": 60,
      "gravidade": 9
    }
  ]
}
```

---

### Buscar pacientes por gravidade

**GET** `/pacientes/gravidade/{gravidade}`

#### Exemplo

```http
GET /pacientes/gravidade/7
```

Retorna todos os pacientes cadastrados com gravidade igual a **7**.

---

## 📁 Estrutura do Projeto

```text
triagem-arvore-binaria/
│
├── main.py
│   └── API FastAPI e definição dos endpoints
│
├── models/
│   └── paciente.py
│
├── tree/
│   └── arvore_binaria.py
│
└── helpers.py
    └── Funções auxiliares para CLI
```

---

## ⚠️ Observações

* A gravidade deve estar entre **0 e 10**.
* A idade deve estar entre **0 e 120 anos**.
* Os dados são armazenados apenas em memória.
* Ao reiniciar o servidor, todos os registros são perdidos.
* O arquivo `helpers.py` foi desenvolvido para uma futura interface de linha de comando (CLI) e atualmente não está integrado à API.

---

## 🎯 Objetivo Educacional

Este projeto foi desenvolvido para demonstrar:

* Estruturas de dados em aplicações reais;
* Implementação de Árvores Binárias de Busca;
* Desenvolvimento de APIs REST com FastAPI;
* Organização de projetos Python em módulos.

---

## 📄 Licença

Este projeto está licenciado sob a licença **MIT**.

---

⭐ Se este projeto foi útil para seus estudos, considere deixar uma estrela no repositório.
