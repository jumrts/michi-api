# Michi API

Backend da aplicação **Michi**, um sistema pessoal para organização de rotina, metas, estudos, finanças e evolução pessoal.

## Stack

- Python 3.12
- FastAPI
- PDM
- PostgreSQL
- Docker

## Executando o projeto

Para iniciar o ambiente:

```bash
pdm run start
```

Esse comando sobe a aplicação utilizando Docker Compose.

## API

A API fica disponível em:

```text
http://localhost:8000
```

## Banco de dados

O projeto utiliza PostgreSQL.

Dentro da rede Docker, a aplicação acessa o banco através de:

```text
postgres:5432
```

## Sobre o projeto

O Michi tem como objetivo centralizar diferentes áreas da vida em uma única aplicação, incluindo:

* Rotina
* Metas
* Finanças
* Estudos
* Progresso pessoal

> 一歩ずつ — Um passo de cada vez.
