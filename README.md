# RocketSeat - Desafio 05

Projeto criado como forma de fixar e avaliar os conhecimentos obtidos no módulo: "Introdução ao Design de Código", quanto aos "Princípios S.O.L.I.D.".
[Desafio proposto](Desafio.txt).

### Funcionalidades

Desafio: Projeto simples de chat por um servidor local com atualização em tempo real.

## Requisitos

- [Python 3.13](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [Docker Desktop](https://docs.docker.com/desktop/)

#### VSCode Extensions recomendadas:
- SQLite Viewer
- MySQL (database-client.com)

## Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/ShiniAkaiUsagi/rocketseat_python_solid_principles.git

# 2. Acesse a pasta do projeto
cd rocketseat_python_solid_principles

# 3. Execute o script de build para preparar as ferramentas e ambiente
sh scripts/build.sh

# O script executa:
# python.exe -m pip install --upgrade pip
# pip install -U poetry
# poetry self update
# poetry update
# poetry run pre-commit install

```
## Tests
PYTHONPATH=. poetry run pytest

## Desafio 5
PYTHONPATH=. poetry run python xxxxx

