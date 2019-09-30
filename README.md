# realtimechatapp
This is my first ever Project working with Django and Docker.
The goal is to build a single channel realtime chat app, that performs sentiment analysis on the messages.

You can see the deployed app here: https://infinite-inlet-33930.herokuapp.com/

### Setting up databases in Docker
1. Postgres 
```
$ docker run --rm --name postgres -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v $HOME/postgres-data:/var/libb/postgresql/data postgres
```
2. Redis 
```
$ docker run --rm --name redis -p 6379:6379 -d redis:2.8`
```

### Install Requirements
`pip install -r requirements.txt`


### To use sentiment-analysis
register for a free account on https://monkeylearn.com/pricing/
then add `chat/sentiment_analysis_config.py` to the project and include your API Key 
(`API_KEY_MONKEYLEARN = '<your API key>'`).


### Commands to get the app started

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver`
