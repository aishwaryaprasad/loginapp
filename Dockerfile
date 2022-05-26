FROM python:3.9.5-slim-buster

# set work directory
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/


# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
CMD python manage.py run -h 0.0.0.0:8000