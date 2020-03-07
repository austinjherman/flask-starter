# FastAPI Starter

This is a starter kit for FastAPI. It's got a FastAPI instance running with Postgres and Alembic. It also has a couple of starter routes. 

## Get Started

This repo is meant to be a starting point for larger projects, so to use it, download the code and set up a new repository.

## Contributing

Feel free to fork it and help me. A lot still needs to be done. And I'm not even sure I'm doing this right.

## Running Locally

Make sure you have [Docker Desktop](https://www.docker.com/products/docker-desktop) installed. From the project root, run `docker-compose up -d` to run in the foreground and `docker-compose up` to run in the background. This will boot up the FastAPI, Postgres, and volume containers. Your FastAPI instance should be running at localhost:2000. Thanks to the work done by FastAPI, you also have documentation about the starter routes at localhost:2000/docs and localhost:2000/redoc.

## Migrations with Alembic

To handle migrations, we have to go into the container that's running the app. So, in a terminal, we have to `docker container ls` and find the container ID that's running fastapi_api. Once we have the container ID, we can do `docker container exec -it <container ID> bash`. 

Once running bash in the container, run `cd server` to get into the server directory. The quirk here is that I haven't been able to figure out how to import things from server/app into the server/migrations directory (according to trying to run the alembic command). So, to use the alembic command, we just need to prefix the command with `PYTHONPATH=.`.

To to the initial migration then, we can do something like `PYTHONPATH=. alembic revision -m "initial migration"`, then `PYTHONPATH=. alembic upgrade head`.