# Architecture of the Michi API

The Michi API follows a Clean Architecture approach, separating business logic
from frameworks, infrastructure, and external services. Dependencies always
point inward: `presentation` depends on `application`, which depends on
`domain`. `infrastructure` also depends on `domain` (by implementing its
contracts), but `domain` never depends on anything outside itself.

```
src/
├── application/
│ └── services/
├── domain/
│ ├── entities/
│ └── contracts/
├── infrastructure/
│ └── database/
│ ├── models/
│ └── repository/
└── presentation/
└── api/
```

## Main

The entry point of the application is `main.py`. It is responsible for
creating the FastAPI app, registering routes, and wiring up dependencies.
Business logic must never be implemented directly inside `main.py`.

## Domain

The `domain` layer holds the core business logic of the application. It must
remain independent from frameworks, databases, and external services — it
cannot depend on FastAPI, SQLAlchemy, PostgreSQL, or any other
infrastructure-related technology.

### Entities

Entities represent the main business objects of the application. They hold
state, behavior, and the business rules tied to that state. Examples in
Michi include `Task`, `Goal`, `Transaction`, and `StudySession`.

An entity can combine data and behavior. For example, `Task` holds a
`complete()` method that enforces the rule that a task cannot be completed
twice — the rule lives on the entity, not in the layers around it.

### Contracts

Contracts define the interfaces the application layer depends on. They
describe *what* an implementation must provide, not *how* — for example,
`TaskRepository` declares `save()` and `get_by_id()` without knowing whether
the data lives in PostgreSQL, memory, or anywhere else. This is what keeps
the domain decoupled from any specific persistence technology.

## Application

The `application` layer contains the use cases of the system: it orchestrates
the flow between entities and contracts. Services are grouped by entity
(e.g. `TaskService`, `GoalService`) rather than one file per use case — each
service receives its repository contract through the constructor and exposes
one method per action (`create`, `complete`, `delete`, ...).

The application layer owns the *flow* of an operation (fetch, validate,
persist); the *business rules* themselves stay in the domain whenever
possible — application code should read like a sequence of steps, not a
place where new rules get invented.

## Infrastructure

The `infrastructure` layer contains the technical implementations the
application depends on — everything that talks to external systems and
technologies.

### Database

The `database` folder holds the SQLAlchemy plumbing: the declarative `Base`
all models inherit from, the `engine`/session setup (`get_db`), and the
`models/` themselves — the classes that map directly to database tables
(e.g. `TaskModel`). This is infrastructure detail; nothing here is imported
by `domain` or `application`.

### Repositories

Repositories implement the contracts defined by the domain. The domain
declares the required behavior; infrastructure provides the concrete
implementation (e.g. `SQLAlchemyTaskRepository`), using the models and
session from `database/` internally. This separation is what makes it
possible to swap the persistence technology without touching the core
business logic.
## Presentation

The `presentation` layer exposes the application to the outside world. A
route's only responsibilities are: receive the request, call the appropriate
application service, and return the response — no business rules or SQL
belong here.

## Benefits

This architecture provides:

- clear separation of responsibilities
- reduced coupling between business logic and frameworks
- easier unit testing
- easier replacement of infrastructure components
- better maintainability as the project grows
- a more organized, scalable codebase