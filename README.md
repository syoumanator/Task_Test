# Онлайн платформа торговой сети электроники

## Стек технологий:
- Backend: Django и Django Rest Framework (DRF) для реализации проекта.
- База данных: PostgreSQL для хранения данных.
- Качество кода: Весь код храниться в удаленном Git репозитории. Соблюден PEP8.

## Установка

1. Клонируйте репозиторий

```bash
git clone https://github.com/syoumanator/Task_Test.git
```

2. Установите зависимости

```bash
pip install -r requirements.txt
```

3. Создайте файл .env и заполните по образцу .sample_env

4. Примените миграции

```bash
python manage.py migrate
```

5. Создайте суперпользователя

```bash
python manage.py csu
```

6. Запустите проект
```bash
python manage.py runserver
```

# Адрес: http://127.0.0.1:8000
