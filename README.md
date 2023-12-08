# работа по DRF
python manage.py createsuper - для создания пользователя\
celery -A config worker -l INFO (добавить -P eventlet - для windows) - запуск задач\
Необходимые настройки для переменных окрежения лежат в env.sample\
Список зависимостей в requirments.txt\
Для запуска программы в docker-compose ввести команду docker-compose up --build\
Для создания базы данных в .env_sample введите свои данные. В терминале введите: psql -U (имя пользователя ) -d (имя основной базы) и через команду create database (имя вашей базы); создайте базу данных.

