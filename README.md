API для системы опросов пользователей.

Загрузка
$ git clone https://github.com/jim95022/poll-api.git

Установка
$ cd poll-api && virtualenv venv --python=3.8 && . venv/bin/activate && pip install -r requirements.txt

Настройка Dgango REST framework
$ cd test_engine

$ ./manage.py migrate

Создадим админ пользователя
$ ./manage.py createsuperuser

Заупуск
$ ./manage.py runserver
Работа с API
{
    "api/poll": "http://127.0.0.1:8000/api/poll/",
    "api/questions": "http://127.0.0.1:8000/api/questions/",
    "api/results": "http://127.0.0.1:8000/api/results/"
}
GET /api/poll/ для получения всех опросов с id вопросами GET /api/questions/ для получения списка всех вопросов GET /api/questions/ для получения вопроса с

GET /api/results/user/id для ответов пользователя

Добавить ответ на вопрос

POST api/results/

{
    "user": null,
    "poll_name": "",
    "result": ""
}
вход в админ кабинет
Добавить новый опрос POST admin/tests/poll/add/

{
    "qstns": [],
    "slug": "",
    "title": "",
    "end_date": null,
    "description": ""
}
