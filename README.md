# Initially Zero

API desenvolvida com **FastAPI** para praticar a criação de endpoints, modelos de dados e testes automatizados.

## Tecnologias e versões configuradas

- Python `>=3.14,<4.0`
- FastAPI `>=0.165.0,<0.166.0`
- Poetry `>=2.0.0` para o gerenciamento de dependências
- Pydantic para validação e serialização dos dados
- Ruff `>=0.17.6,<0.18.0` para lint e formatação
- pytest `>=9.2.0,<10.0.0`
- pytest-cov `>=7.1.0,<8.0.0`
- taskipy `>=1.14.1,<2.0.0`

As dependências estão registradas em `pyproject.toml` e fixadas em `poetry.lock`.

## Estrutura do projeto

```text
initially_zero/
├── initially_zero/
│   ├── __init__.py
│   ├── app.py
│   └── schemas.py
├── tests/
│   ├── __init__.py
│   └── test_app.py
├── htmlcov/
├── pyproject.toml
├── poetry.lock
└── README.md
```

## Instalação

Na raiz do projeto, instale as dependências:

```bash
poetry install
```

Certifique-se de que o ambiente está usando uma versão de Python compatível:

```bash
poetry env use 3.14
```

## Executando a aplicação

Por meio do taskipy:

```bash
poetry run task run
```

Ou diretamente com FastAPI:

```bash
poetry run fastapi dev initially_zero/app.py
```

A aplicação pode ser acessada em `http://127.0.0.1:8000`. A documentação interativa fica disponível em:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Endpoints

### `GET /`

Retorna uma mensagem de boas-vindas.

Resposta com status `200 OK`:

```json
{
  "message": "Olá, mundo!"
}
```

### `POST /users/`

Cadastra um usuário em uma lista em memória.

Corpo da requisição:

```json
{
  "userName": "João",
  "userEmail": "joao@example.com",
  "userPassword": "senha-segura"
}
```

Resposta com status `201 Created`:

```json
{
  "userName": "João",
  "userEmail": "joao@example.com",
  "userId": 1
}
```

O campo `userPassword` não é incluído na resposta pública. Os dados são armazenados apenas na variável `database` durante a execução da aplicação e são perdidos ao reiniciar o processo.

## Modelos Pydantic

- `Message`: mensagem retornada pela rota raiz.
- `UserSchema`: dados enviados na criação do usuário, incluindo nome, e-mail e senha.
- `UserSchemaPublic`: dados públicos retornados pela API, sem a senha.
- `UserDB`: modelo interno usado para armazenar os dados do usuário com seu identificador.

O campo `userEmail` é validado pelo tipo `EmailStr`.

## Configuração do Ruff

O Ruff está configurado em `pyproject.toml` com:

- Comprimento máximo de linha: `79`
- Preview habilitado para lint e formatação
- Diretório `migrations` excluído da análise
- Aspas simples no formato automático
- Regras selecionadas: `I`, `F`, `E`, `W`, `PL` e `PT`

Comandos disponíveis:

```bash
poetry run task lint
poetry run task format
```

Antes da formatação, o taskipy executa `ruff check --fix`.

## Configuração do pytest

O pytest está configurado para:

- Adicionar o diretório atual ao `pythonpath`
- Desativar o plugin de avisos (`-p no:warnings`)
- Executar os testes com o cliente de testes do FastAPI
- Coletar cobertura do pacote `initially_zero`

Os testes estão em `tests/test_app.py`. O teste atual verifica:

- A resposta da rota `GET /`
- O JSON retornado pela rota
- O status HTTP `200 OK`

## Comandos de tarefa

As tarefas estão configuradas no taskipy:

| Comando | Ação |
|---|---|
| `poetry run task lint` | Executa o Ruff em todo o projeto |
| `poetry run task format` | Corrige lint e formata os arquivos |
| `poetry run task run` | Inicia a aplicação FastAPI em modo de desenvolvimento |
| `poetry run task test` | Executa lint, testes, cobertura e relatório HTML |

O comando de testes executa internamente:

```bash
pytest -s -x --cov=initially_zero -vv
```

Após os testes, o relatório de cobertura HTML é gerado na pasta `htmlcov/` pelo hook `post_test`.