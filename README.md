# 📂 FileManagerNew

FastAPI-приложение для управления файлами и пользователями.  
Используется **FastAPI**, **SQLAlchemy ORM**, **JWT-аутентификация**.  

---

## 🚀 Возможности
- 🔑 Авторизация и регистрация пользователей (JWT-токены).  
- 📁 Загрузка и скачивание файлов.  
- 🗂️ CRUD-операции с файлами и пользователями.  
- 🔒 Защита эндпоинтов через токены.  
- 📜 Логи операций.  

---

## 🛠️ Стек технологий
- [FastAPI](https://fastapi.tiangolo.com/) – backend-фреймворк  
- [SQLAlchemy ORM](https://www.sqlalchemy.org/) – работа с базой данных  
- [Pydantic](https://docs.pydantic.dev/) – валидация данных  
- [JWT](https://jwt.io/) – аутентификация  
- [Uvicorn](https://www.uvicorn.org/) – ASGI-сервер  

---

## 📂 Структура проекта
```
app/
 └── src/
      ├── api.py               # Точка входа FastAPI
      ├── models/              # SQLAlchemy модели
      ├── routers/             # Эндпоинты
      ├── servises/            # Сервисы (работа с токенами, БД и т.д.)

```

---

## ⚙️ Установка и запуск

### 1. Клонировать репозиторий
```bash
git clone https://github.com/MyDev-bit/FileManagerNew.git
cd FileManagerNew/app/src
```

### 2. Создать и активировать виртуальное окружение
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Установить зависимости
```bash
pip install -r requirements.txt
```

### 4. Запуск сервера
```bash
uvicorn api:app --reload
```

---

## 📖 API Документация
После запуска:  
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)  
- Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)  

---

## ✅ TODO (план улучшений)
- [ ] Добавить Alembic миграции  
- [ ] Написать тесты (pytest)  
- [ ] Подключить Docker + docker-compose  
- [ ] Добавить CI/CD (GitHub Actions / GitLab CI)  
- [ ] Улучшить логирование и обработку ошибок  

---

## 👨‍💻 Автор
Разработчик: [MyDev-bit](https://github.com/MyDev-bit)


