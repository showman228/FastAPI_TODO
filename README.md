# FastAPI TODO

Пет-проект — сервис для управления задачами и заметками с REST API на FastAPI и асинхронной работой с PostgreSQL через SQLAlchemy 2.0. Включает простой веб-фронтенд (регистрация/вход и список заметок).

## Стек технологий

- **Python 3.13**
- **FastAPI** — веб-фреймворк для REST API
- **SQLAlchemy 2.0 (async)** + **asyncpg** — асинхронный доступ к PostgreSQL
- **Pydantic v2** / **pydantic-settings** — валидация данных и конфигурация
- **Uvicorn** — ASGI-сервер
- **Poetry** — управление зависимостями
- **Docker / Docker Compose** — контейнеризация
- Frontend — HTML/CSS/JS без фреймворков

## Возможности

**Пользователи**
- Регистрация и вход (`POST /users`, `POST /users/login`)
- Получение списка пользователей и пользователя по id
- Обновление и удаление профиля

**Задачи / заметки**
- Создание, получение, обновление и удаление задач
- Получение всех задач конкретного пользователя (`GET /tasks/user/{user_id}`)

Интерактивная документация API (Swagger UI) доступна на `/docs` после запуска сервера.

<img width="585" height="271" alt="Screenshot 2026-07-16 at 15 54 28" src="https://github.com/user-attachments/assets/3184b302-e535-45f8-9739-19dbff6883ff" />
<img width="1555" height="792" alt="Screenshot 2026-07-16 at 15 55 16" src="https://github.com/user-attachments/assets/50634f18-e972-42a9-8c3f-66239e9b4a09" />
<img width="1560" height="797" alt="Screenshot 2026-07-16 at 15 55 25" src="https://github.com/user-attachments/assets/746c9f28-2917-4891-97f7-16489fde55f8" />
<img width="1595" height="932" alt="Screenshot 2026-07-16 at 15 53 37" src="https://github.com/user-attachments/assets/97786348-f7ee-45a2-bca1-531e6313caf9" />
<img width="362" height="536" alt="Screenshot 2026-07-16 at 15 53 49" src="https://github.com/user-attachments/assets/99f36362-9c4f-4720-8a76-577bd8a09db2" />
<img width="367" height="440" alt="Screenshot 2026-07-16 at 15 53 48" src="https://github.com/user-attachments/assets/03c4f8da-5fb1-4385-bae9-963738266849" />


## Структура проекта

```
FastAPI_TODO/
├── backend/
│   ├── app/
│   │   ├── models/          # SQLAlchemy-модели (User, Task)
│   │   ├── schemas/          # Pydantic-схемы
│   │   ├── repositories/     # Слой доступа к данным
│   │   ├── services/         # Бизнес-логика
│   │   ├── router/           # FastAPI-роутеры
│   │   ├── config.py         # Настройки (pydantic-settings)
│   │   ├── database.py       # Подключение к БД, сессии
│   │   └── main.py           # Точка входа приложения
│   ├── run.py                # Локальный запуск через uvicorn
│   └── Dockerfile
├── frontend/
│   └── assets/                # Статика: страницы входа, регистрации, заметок
├── docker-compose.yml
├── pyproject.toml
└── poetry.lock
```

## Запуск проекта

### Вариант 1: Docker Compose (рекомендуется)

1. Создайте файл `backend/.env` со следующими переменными:

   ```env
   DB_HOST=db
   DB_PORT=5432
   DB_NAME=Todo
   DB_USER=postgres
   DB_PASS=postgres
   ```

2. Запустите контейнеры:

   ```bash
   docker compose up --build
   ```

3. Приложение будет доступно на [http://localhost:8000](http://localhost:8000), документация API — на [http://localhost:8000/docs](http://localhost:8000/docs).

### Вариант 2: Локально через Poetry

1. Убедитесь, что PostgreSQL запущен локально, и создайте базу данных.
2. Создайте файл `backend/.env`:

   ```env
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=Todo
   DB_USER=postgres
   DB_PASS=postgres
   ```

3. Установите зависимости:

   ```bash
   poetry install
   ```

4. Запустите сервер из директории `backend`:

   ```bash
   cd backend
   poetry run python run.py
   ```

   либо напрямую через uvicorn:

   ```bash
   poetry run uvicorn app.main:app --reload
   ```

## Модели данных

**User** — `id`, `username`, `email`, `password`, `firstname`, `lastname`, `created_at`

**Task** — `id`, `name`, `description`, `created_at`, `user_id` (связь с пользователем)

## Планы по доработке

- [ ] Хеширование паролей и полноценная аутентификация (JWT)
- [ ] Валидация и разделение прав доступа между пользователями
- [ ] Покрытие тестами

## Автор

[showman228](https://github.com/showman228)

## Лицензия

MIT
