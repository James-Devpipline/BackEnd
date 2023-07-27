FROM python:3.10

RUN pip install --upgrade pip

RUN mkdir /app
COPY . /app

RUN useradd -ms /bin/bash worker
RUN chown -R worker:worker /app
#change owner, recursive, full acces to worker user and group, into the app directory