
# Это пример бекенда, основанного на Django + stripe api.
В ТЗ используется такие технологии как Python, Docker, stripe, PostgreSQL. 


# Как запустить весь проект?

### Первый способ. Через Docker.

Скачав проект с гитхаба напишите в командную строку 


```bash
docker-compose up -d

```
```
docker-compose run web python manage.py migrate  
```
```
docker-compose run web python manage.py createsuperuser
```

```bash
docker-compose up   
```
Вы можете добавить флаг -d к команде, чтобы запустить контейнеры в фоновом режиме. 

```bash
docker-compose up -d  
```
После запуска переходим на страницу админа http://127.0.0.1:8000/admin
Добавляем в item товар.
После переходим на главную страницу http://127.0.0.1:8000
и выбираем наш товар. можно нажать на его наименование и пройти по ссылке
 http://127.0.0.1:8000item/<id> заменив id на id товара на пример 1
При нажатии на кнопку купить, происходит обработка запроса описанная в ТЗ 
```Коммент
GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. 
При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
```

### Второй способ. Вручную через localhost. Для этого способа нужно установить postgresql и указать ваш пароль и имя бд. Ну или воспользоваться SQLite. 

Прежде всего вам нужно создать файл .env и добавить туда следующие значения.
```
STRIPE_PUBLIC_KEY = "pk_test_..."
STRIPE_SECRET_KEY = "sk_test_..."
DB_NAME = "db"
DB_USER = "postgres"
DB_PASSWORD = "Password"
DB_HOST = "localhost"
DB_PORT = "5432"

``` 

Создаем виртуально окружение. 
```bash
python -m venv venv

venv\Scripts\Activate.ps1
```

#### Установите все зависимости из requirements.txt написав:
```bash
pip install -r requirements.txt
```

#### Затем последовательно введите:
```bash
cd ApiApp
```
#### Проведите миграции.
```bash
python manage.py makemigrations
python manage.py migrate
```
#### Создайте админа.
```bash
python manage.py createsuperuser 
```


#### После регистрации запустите локальный сервер.
```bash
python manage.py runserver
```
#### Затем перейдите по ссылке http://127.0.0.1:8000/admin
После запуска переходим на страницу админа http://127.0.0.1:8000/admin
Добавляем в item товар.
После переходим на главную страницу http://127.0.0.1:8000
и выбираем наш товар. можно нажать на его наименование и пройти по ссылке
 http://127.0.0.1:8000item/<id> заменив id на id товара на пример 1
При нажатии на кнопку купить, происходит обработка запроса описанная в ТЗ 
```Коммент
GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. 
При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
```


#### Все дополнительные задания были реализованы. 
 


# Приятного использования.    
