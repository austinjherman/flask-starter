FROM python:3-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/server

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt --trusted-host=files.pythonhosted.org

COPY . .

RUN chmod +x ./scripts/start.sh

EXPOSE 80