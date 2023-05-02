# Important: есть возможность запустить с помощью Docker:

## 1. Укажите нижеперечисленные параметры в .env
POSTGRES_DB (название бд),

POSTGRES_USER (имя пользователя),

POSTGRES_PASSWORD (пароль пользователя)

## 2. Запустите Docker Image

`docker compose build`

`docker compose up -d`

# Инструкция по запуску без Docker
## 1. Склонируйте репозиторий

`git clone https://github.com/vyual/task_manager`

## 2. Создайте venv

`cd task_manager/`
`python -m venv`

## 3. Установите зависимости

`pip install -r requirements.txt`

## 4. Укажите параметры подключения к базе

### 1. Переименуйте файл окружения `.env.dist` в `.env`
### 2. Измените `DATABASE_URL`
### 3. Укажите остальные параметры
POSTGRES_DB (название бд),

POSTGRES_USER (имя пользователя),

POSTGRES_PASSWORD (пароль пользователя)


