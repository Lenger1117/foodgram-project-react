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
<h2 dir="auto" tabindex="-1">Инструкции по установке локально:</h2>
<ol>
<li>Клонируйте проект: <code><code>git clone&nbsp;</code></code><code>https://github.com/Lenger1117/foodgram-project-react.git</code></li>
<li><em><strong>Установите и активируйте виртуальное окружение:</strong></em></li>
<li><em><strong>Установите зависимости из файла requirements.txt:</strong></em></li>
<li><em><em><strong>В папке с файлом manage.py примените миграции:&nbsp;</strong></em></em><code>python manage.py migrate</code></li>
<li><em><em><strong>В папке с файлом manage.py выполните команду для запуска локально:&nbsp;</strong></em></em><code></code><code>python manage.py runserver</code></li>
<li><em><em><strong>Локально документацию можно посмотреть по адресу:&nbsp;</strong></em></em><code></code><code>http://127.0.0.1/api/docs/</code></li>
</ol>
<hr />
<h2 dir="auto" tabindex="-1">Инструкции по установке на удаленном сервере:</h2>
<ol>
<li>Скопируйте на сервер необходимые файлы:</li>
<li>Установите docker и docker-compose:</li>
<li>Соберите контейнер: <code>sudo docker-compose up -d --build</code></li>
<li>Выполните миграции: <code>sudo docker-compose exec backend python manage.py migrate</code></li>
<li>Соберите статику: <code>sudo docker-compose exec backend python manage.py collectstatic --no-input</code></li>
<li>Создайте суперюзера: <code>sudo docker-compose exec backend python manage.py createsuperuser</code></li>
<li>Наполните базу данных ингредиентами и тегами: sudo&nbsp;docker-compose exec backend python manage.py load_data<br /><code></code><br /><code></code><br /><code></code></li>
</ol>
<p>&nbsp;</p>
<p><code></code></p>