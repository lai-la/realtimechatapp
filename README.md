# realtimechatapp
This is my first ever Project working with Django and docker, trying to build a single channel realtime chat app.

### Setting up databases in docker
1. Postgres 
```
$ sudo docker run --rm --name postgres -e POSTGRES_PASSWORD=docker -d -p 5432:5432 
-v $HOME/postgres-data:/var/libb/postgresql/data postgres
```
2. Redis 
```
$ docker run -p 6379:6379 -d redis:2.8`
```


### Commands to get the app started

`$ python manage.py makemigrations`

`$ python manage.py migrate`

`$ python manage.py runserver`
