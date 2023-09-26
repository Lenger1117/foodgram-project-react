## Опиcание проекта
Сайт Foodgram, «Продуктовый помощник». Это онлайн-сервис и API для него. На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

## Проект доступен по ссылкам:

```
https://lenger1117.ddns.net/
```
```
http://158.160.15.64/
```
```
http://158.160.15.64/admin/
```
```
http://158.160.15.64/api/docs/
```

## Данные для проверки работы приложения (суперюзер):

```
- email: admin@admin.ru
- password: 89tofomo
```

## Инструкции по установке локально:
# 1. Клонируйте проект:
```
git clone https://github.com/Lenger1117/foodgram-project-react.git
```
# 2. Установите и активируйте виртуальное окружение:
```
python3 -m venv venv или python -m venv venv
```
```
source venv/bin/activate или source venv/Scripts/activate
```
# 3. Установите зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
# 4. В папке с файлом manage.py примените миграции:
```
python manage.py migrate
```
# 5. В папке с файлом manage.py выполните команду для запуска локально:
```
python manage.py runserver
```
# 6. Локально документацию можно посмотреть по адресу:
```
http://127.0.0.1/api/docs/
```

<h3 dir="auto" tabindex="-1">Опиание проекта.</h3>
<p dir="auto">Сайт Foodgram, &laquo;Продуктовый помощник&raquo;. Это онлайн-сервис и API для него. На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список &laquo;Избранное&raquo;, а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.</p>
<hr />
<h2 dir="auto" tabindex="-1">Проект доступен по ссылкам:</h2>
<ul>
<li>
<pre class="notranslate"><code>http://123/</code></pre>
</li>
<li>
<pre class="notranslate"><code>http://123/admin/</code></pre>
</li>
<li>
<pre class="notranslate"><code>http://123/api/docs/</code></pre>
</li>
</ul>
<p><code></code></p>
<hr />
<p><code></code></p>
<h2 dir="auto" tabindex="-1">Данные для проверки работы приложения (суперюзер):</h2>
<pre class="notranslate"><code>email: admin@admin.ru
password: 89tofomo</code></pre>
<hr />
<pre class="notranslate"><code></code></pre>
<h2 dir="auto" tabindex="-1">Инструкции по установке локально:</h2>
<ol>
<li><em><strong>Клонируйте проект: </strong></em><code><code>git clone&nbsp;</code></code><code>https://github.com/Lenger1117/foodgram-project-react.git</code><strong><code></code></strong><em><strong><code></code></strong></em></li>
<li><em><em><strong>Установите и активируйте виртуальное окружение:&nbsp;</strong></em></em><code>python3 -m venv venv (или&nbsp;</code><code>python -m venv venv)&nbsp;/&nbsp;</code><code>source venv/bin/activate (или&nbsp;</code><code>source venv/Scripts/activate)</code><code></code><code></code><code></code></li>
<li><em><em><strong>Установите зависимости из файла requirements.txt:&nbsp;</strong></em></em><code>pip install -r requirements.txt</code></li>
<li><em><strong>В папке с файлом manage.py примените миграции:&nbsp;</strong></em><code>python manage.py migrate</code></li>
<li><em><strong>В папке с файлом manage.py выполните команду для запуска локально:&nbsp;</strong></em><code>python manage.py runserver</code></li>
<li><em><strong>Локально документацию можно посмотреть по адресу:&nbsp;</strong></em><code>http://127.0.0.1/api/docs/</code></li>
</ol>
<hr />
<h2 dir="auto" tabindex="-1">Инструкции по установке на удаленном сервере:</h2>
<ol>
<li><em><strong>Скопируйте на сервер необходимые файлы:</strong></em></li>
<li><em><strong>Установите docker и docker-compose:&nbsp;</strong></em><code>sudo apt install docker.io 
sudo apt install docker-compose</code></li>
<li><em><strong>Соберите контейнер: </strong></em><code>sudo docker-compose up -d --build</code></li>
<li><em><strong>Выполните миграции: </strong></em><code>sudo docker-compose exec backend python manage.py migrate</code></li>
<li><em><strong>Соберите статику: </strong></em><code>sudo docker-compose exec backend python manage.py collectstatic --no-input</code></li>
<li><em><strong>Создайте суперюзера: </strong></em><code>sudo docker-compose exec backend python manage.py createsuperuser</code></li>
<li><em><strong>Наполните базу данных ингредиентами и тегами: </strong></em>sudo&nbsp;docker-compose exec backend python manage.py load_data<code></code><code></code><code></code></li>
</ol>
<p><code></code></p>
