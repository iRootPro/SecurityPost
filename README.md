# SecurityPost

Данный скрипт работает и выводит через web интерфейс информацию о пользователях хранилища. Показывает информаию о пользователях, их визитах, а также определяет подозрительность.

## Как установить

Python3 должен быть уже установлен в системе.  
Используя `pip` или  `pip3`  (если есть конфликт с python2) необходимо установить  зависимости:

```shell
pip install -r requirements.txt
```

Необходимо использовать виртуальное окружение для изоляции проекта.  
Подробности: [virtualenv/venv](https://docs.python.org/3/library/venv.html).

## Настройка доступа к Базе Данных

Для настройки доступа к БД необходимо в корне с проектом создать файл `.env`, в котором прописать данные:

```
DB_HOST=АДРЕС_СЕРВЕРА_БД
DB_PORT=ПОРТ_СЕРВЕРА_БД
DB_NAME=ИМЯ_БЖ
DB_USERNAME=ИМЯ_ПОЛЬЗОВАТЕДЯ_БД
DB_PASSWORD=ПАРОЛЬ
DJANGO_DEBUG=TRUE_ИЛИ_FALSE
DJANGO_SECRET_KEY=СЕКРЕТНЫЙ_КЛЮЧ
```

*DJANGO_DEBUG* отвечает за вывод отладочной информации.
При значении **True** - отладочная информация выводится.
При значении **False** - отладочная информация не выводится.


## Запуск скрипт

Для запуска скрипта в командной строке нужно ввести команду:

```shell
python3 manage.py runserver 0.0.0.0:8000
```

В терминале будет указано, что Django сервер успешно запущен, а также будет указана ссылка, по которой можно перейти в браузере.

Введите в браузере адрес: [http://0.0.0.0:8000](http://0.0.0.0:8000).

Вы увидите web страницу со всеми необходимыми данными.

## Цель проекта

Данные скрипты написаны только с образовательной целью. 