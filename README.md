# API к учебному проекту для изучения FastAPI

## Интсрументы и технологии
![](https://img.shields.io/badge/python-3.11-blue)
![](https://img.shields.io/badge/FastAPI-0.88-green)
![](https://img.shields.io/badge/uvicorn-0.20-yellow)
![](https://img.shields.io/badge/SQLAlchemy-1.4-orange)
![](https://img.shields.io/badge/pytest-7.2-lightgrey)

В проекте доступна аутентификация по Bearer Токену. Позволяет пользователям просматривать посты и статьи других пользователей, а так же создавать свои. В проекте осуществлены такие тестовые концепты разработки, как: Логирование, Тестирование, Асинхронные запросы к API, Вебсокеты, настройка CORS для отношения между бекендом и фронтендом

## Установка проекта локально
#### Клонировать проект 
```sh
https://github.com/AltyOfficial/my-fastapi.git
```
#### Создать и установить виртуальное окружение, установить зависимости
```sh
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```
#### Перейти в директорию с проектом и запустить сервер
```sh
cd backend/
uvicorn main:app --reload
```

