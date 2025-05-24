# 🧼 Clean Architecture com FastAPI - Projeto Didático

Este projeto visa **praticar os princípios da Clean Architecture** utilizando o
framework **FastAPI**, com uma implementação simples e focada no aprendizado.

Toda a estrutura foi pensada para separar claramente as camadas da aplicação:
adaptadores (interfaces com o mundo externo), casos de uso, entidades e interfaces.

---

## 📁 Estrutura do Projeto

```bash
.
├── main.py                                 # Ponto de entrada da aplicação
├── pyproject.toml                          # Dependências (usando UV)
├── requirements.txt                        # Dependências (alternativa com pip)
├── uv.lock                                 # Lockfile de versões (gerado pelo UV)
└── src/                                    # Código-fonte principal da aplicação
    ├── adapters/                           # Camada de entrada (interfaces externas)
    │   └── http/                           # Interface HTTP (FastAPI)
    │       ├── dto/                        # Modelos de entrada e saída da API
    │       │   └── user_dtos.py            # DTOs com UserRequest e UserResponse
    │       └── routers/                    # Rotas da aplicação
    │           └── user_change_last_name_router.py  # Rota POST /users/register
    ├── application/                        # Camada de aplicação (casos de uso)
    │   └── use_cases/                      # Implementações dos casos de uso
    │       └── user_change_last_name_use_case.py    # Lógica de alteração do sobrenome
    └── domain/                             # Camada de domínio (regra de negócio)
        ├── entities/                       # Entidades da regra de negócio
        │   └── user_entity.py              # Entidade que representa o usuário
        └── interfaces/                     # Contratos da camada de domínio
            └── user_change_last_name_interface.py  # Interface do caso de uso
```

---

## 🧠 Objetivo

- Aplicar os conceitos da **Clean Architecture**:
    - Independência de frameworks
    - Separação de camadas
    - Lógica de negócio isolada
- Entender o fluxo entre DTOs → Casos de Uso → Entidades → Respostas
- Estudar práticas de design para manter o código desacoplado

---

## 🚀 Como Executar

### ▶️ Opção 1: Usando `uv`

```bash
uv sync
```

```bash
uv run python main.py
```

### ▶️ Opção 2: Usando `python` e `pip`

```bash
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual:
# No Linux/macOS:
source venv/bin/activate

# No Windows:
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Rode o servidor
python main.py
```

---

## 🧪 Funcionalidade Atual

### ✅ Alteração de Sobrenome do Usuário

A aplicação implementa uma funcionalidade simples:

- Endpoint: `POST /users/register`
- Recebe um JSON com `first_name` e `last_name`
- **Ignora o sobrenome fornecido** e substitui por `"New Last Name"`
- Retorna os dados atualizados

#### 🔄 Exemplo

**Requisição:**

```json
{
  "first_name": "Lucas",
  "last_name": "Original"
}
```

**Resposta:**

```json
{
  "first_name": "Lucas",
  "last_name": "New Last Name"
}
```

Essa lógica é propositalmente simplificada para focar na **arquitetura e
organização do código**, não na regra de negócio em si.

---

## 🧱 Fluxo da Aplicação

```text
[ FastAPI Router (HTTP) ]
         ↓
[ DTO (UserRequest) ]
         ↓
[ Use Case (UserChangeLastNameUseCase) ]
         ↓
[ Entidade (UserEntity) ]
         ↓
[ DTO (UserResponse) ]
         ↓
[ Resposta HTTP ]
```

- **`UserRequest`**: representa os dados de entrada da requisição
- **`UserChangeLastNameUseCase`**: aplica a lógica de mudança do sobrenome
- **`UserEntity`**: representa o usuário como entidade de domínio
- **`UserResponse`**: estrutura da resposta JSON

---

## 📘 Documentação Swagger (gerada automaticamente)

Ao rodar a aplicação, a FastAPI disponibiliza uma documentação interativa via Swagger UI.

- **Swagger UI:**  
  Acesse em [http://localhost:8000/docs](http://localhost:8000/docs)

- **ReDoc (alternativa):**  
  Acesse em [http://localhost:8000/redoc](http://localhost:8000/redoc)

Essas interfaces permitem testar os endpoints e visualizar os esquemas de requisição e resposta definidos com Pydantic.

---

## 🛠️ Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- Python 3.13+
- Clean Architecture (Robert C. Martin)
- [Uvicorn](https://www.uvicorn.org/)
- [UV](https://docs.astral.sh/uv/guides/install-python/)

---

## 📚 Observações

> Este projeto é **estritamente educacional**. Não possui banco
> de dados, autenticação, testes ou persistência.  
> O foco está na organização arquitetural e separação de
> responsabilidades.

---

## 👨‍💻 Autor

**Lucas Praciano**  
[LinkedIn](https://www.linkedin.com/in/lucas-praciano-420552210/) |
[GitHub](https://github.com/lspraciano)
