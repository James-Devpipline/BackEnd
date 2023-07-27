FROM python:3.10

RUN pip install --upgrade pip

RUN mkdir /app
COPY . /app

RUN useradd -ms /bin/bash worker
RUN chown -R worker:worker /app
#change owner, recursive, full acces to worker user and group, into the app directory

USER worker
# switching to worker user we creacted
WORKDIR /app
# specifies where app is in container, so all files are executed in this folder
ENV PATH="/home/worker/.local/bin:$PATH" 
# specifies env for this container, update path variable so it can be utilized, directory where things get stored

RUN pip install pipenv
RUN pipenv install
RUN PIPENV INSTALL gunicorn

RUN chmod +X ./entrypoint.sh
# change mod, we want this to eXecutable
CMD ["sh", "entrypoint.sh"]
# shell script, tell docker to run the entrypoint.sh file as soon as the container starts
