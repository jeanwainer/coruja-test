FROM python:3.8-alpine
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY . /app
WORKDIR /app
ENTRYPOINT ["sh", "docker-entrypoint.sh"]