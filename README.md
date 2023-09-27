# Опиcание проекта
Сайт Foodgram, «Продуктовый помощник». Это онлайн-сервис и API для него. На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

# Стек проекта:
- Python
- Django
- Docker

# Проект доступен по ссылкам:
```
https://lenger1117.ddns.net/
```
```
https://lenger1117.ddns.net/admin/
```
```
http://158.160.15.64/
```
```
http://158.160.15.64:8000/admin/
```

# Данные для проверки работы приложения (суперюзер):
```
- email: admin@admin.ru
- password: 89tofomo
```




# Инструкции по установке локально:
### 1. Клонируйте проект:
```
git clone https://github.com/Lenger1117/foodgram-project-react.git
```
### 2. Установите и активируйте виртуальное окружение:
```
python3 -m venv venv или python -m venv venv
```
```
source venv/bin/activate или source venv/Scripts/activate
```
### 3. Установите зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
### 4. В папке с файлом manage.py примените миграции:
```
python manage.py migrate
```
### 5. В папке с файлом manage.py выполните команду для запуска локально:
```
python manage.py runserver
```
### 6. Локально документацию можно посмотреть по адресу:
```
http://127.0.0.1/api/docs/
```




# Инструкции по установке на удаленном сервере:
### 1. Скопируйте на сервер необходимые файлы:
```
файлы
```
### 2. Установите docker и docker-compose:
```
sudo apt install docker.io
```
```
sudo apt install docker-compose
```
### 3. Соберите контейнер (в папке /infra):
```
sudo docker-compose up -d --build
```
### 4. Выполните миграции (в папке /infra):
```
sudo docker-compose exec backend python manage.py makemigrations
```
```
sudo docker-compose exec backend python manage.py makemigrations users
```
```
sudo docker-compose exec backend python manage.py makemigrations recipes
```
```
sudo docker-compose exec backend python manage.py migrate
```
### 5. Соберите статику (в папке /infra):
```
sudo docker-compose exec backend python manage.py collectstatic --no-input
```
### 6. Наполните базу данных ингредиентами и тегами (в папке /infra):
```
sudo docker-compose exec backend python manage.py load_data
```

# Примеры запросов API
### Регистрация пользователя:
```
POST https://lenger1117.ddns.net/api/users/
```
```
Запрос:

{
  "email": "vpupkin@yandex.ru",
  "username": "vasya.pupkin",
  "first_name": "Вася",
  "last_name": "Пупкин",
  "password": "89tofomo"
}
```
```
Ответ (201Created):

{
    "first_name": "Вася",
    "last_name": "Пупкин",
    "username": "vasya.pupkin",
    "email": "vpupkin@yandex.ru"
}
```

