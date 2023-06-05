FROM python:3.7.16
USER root

RUN mkdir django

WORKDIR /root/django/

RUN apt-get update
COPY . .

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

CMD ["python", "api_insta/manage.py", "runserver", "0.0.0.0:8000"]
# ENTRYPOINT ["/bin/sh", "-c", "while :; do sleep 10; done"]
