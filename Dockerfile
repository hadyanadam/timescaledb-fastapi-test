FROM python:3.8.6-slim-buster

ENV WORKDIR=/usr/src/app
ENV USER=app
ENV APP_HOME=/home/app/web
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR $WORKDIR

RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile ./Pipfile.lock $WORKDIR/
RUN pipenv lock
RUN pipenv install --system --deploy
# COPY ./requirements.txt $WORKDIR/requirements.txt
# RUN pip install -r requirements.txt

RUN adduser --system --group $USER
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY . $APP_HOME
RUN chown -R $USER:$USER $APP_HOME
USER $USER