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

### To use sentiment-analysis
register for a free account on https://monkeylearn.com/pricing/
then add `chat/sentiment_analysis_config.py` to the project and include your API Key 
(`API_KEY_MONKEYLEARN = '<your API key>'`).


### Commands to get the app started

`$ python manage.py makemigrations`

`$ python manage.py migrate`

`$ python manage.py runserver`
