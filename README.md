API для системы опросов пользователей.

<h2>Загрузка</h2>
<pre>
$ git clone https://github.com/jim95022/poll-api.git
</pre>
<h2>Установка</h2>
<pre>
$ cd poll-api && virtualenv venv --python=3.8 && . venv/bin/activate && pip install -r requirements.txt
</pre>
<h2>Настройка Dgango REST framework</h2>
<pre>
$ cd test_engine

$ ./manage.py migrate
</pre>

<h2>Создадим админ пользователя</h2>
<pre>
$ ./manage.py createsuperuser
</pre>

<h2>Заупуск</h2>
<pre>
$ ./manage.py runserver
</pre>

Работа с API
<pre>
{
    "api/poll": "http://127.0.0.1:8000/api/poll/",
    "api/questions": "http://127.0.0.1:8000/api/questions/",
    "api/results": "http://127.0.0.1:8000/api/results/"
}
</pre>
<pre>
GET /api/poll/ для получения всех опросов с id вопросами 
GET /api/questions/ для получения списка всех вопросов 
GET /api/questions/<id> для получения вопроса с <id>

GET /api/results/user/id для ответов пользователя
</pre>
Добавить ответ на вопрос. Опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
<pre>
POST api/results/
</pre>
<pre>
{
    "user": null,
    "poll_name": "",
    "result": ""
}
</pre>
<h2>вход в админ кабинет</h2>

Админ может:
 - добавленять/измененять/удалять опросовы. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
-  добавленять/измененять/удалять вопросы в опросе. Атрибуты вопросов: текст вопроса, тип вопроса 
Добавить новый опрос 
<pre>
POST admin/tests/poll/add/

{
    "qstns": [],
    "slug": "",
    "title": "",
    "end_date": null,
    "description": ""
}
</pre>


