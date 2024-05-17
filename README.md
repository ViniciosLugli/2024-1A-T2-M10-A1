# 2024-1A-T2-M10-A1

A simple project to manager orders with users, the solution is a REST API using [python](https://www.python.org/), [fastapi](https://fastapi.tiangolo.com/) and [prisma](https://prisma-client-py.readthedocs.io/en/stable/)

## Features

-   Create, read and delete users
-   Create, read, update and delete orders
-   Prisma ORM to manage the database
-   FastAPI to create the REST API
-   Docker to manage the database and the api
-   Swagger documentation
-   Insomnia file to test the api
-   Folder structure to manage the project in a clean way

## Folders:

-   `assets`: Contains the insomina file
-   `prisma`: Contains the prisma schema and the migrations
-   `src/repositories`: Contains the repositories to manage the database
-   `src/routes`: Contains the routes to the api
-   `src/main.py`: Contains the main file to start the api

## Requirements

There are some requirements to run the project:

-   [Docker](https://www.docker.com/)
-   Is recommended to use [insomnia](https://insomnia.rest/) to test the api

## How to run

1. Clone the repository

    ```bash
    git clone git@github.com:ViniciosLugli/2024-1A-T2-M10-A1.git
    ```

2. Enter the project folder

    ```bash
    cd 2024-1A-T2-M10-A1
    ```

3. Run the project docker compose to start the database and the api

    ```bash
    docker compose -f docker-compose.yml up --build
    ```

4. Now you can access the api at [http://localhost:3000](http://localhost:3000) and they documentation at [http://localhost:3000/docs](http://localhost:3000/docs)

You can use the [insomnia](https://insomnia.rest/) to test the api, just import the file [insomnia.json](./assets/Insomnia.json) to your insomnia and you will have all the requests to test the api.

![image](https://github.com/ViniciosLugli/2024-1A-T2-M10-A1/assets/40807526/2bfdc72e-e698-416e-a51a-436668750ee4)

## Demos

### Example API page output

![image](https://github.com/ViniciosLugli/2024-1A-T2-M10-A1/assets/40807526/7a9e2885-d006-434e-bcb7-04dcbbf75522)

### Example usage using [insomnia](https://insomnia.rest/)

[demo.webm](https://github.com/ViniciosLugli/2024-1A-T2-M10-A1/assets/40807526/1485ff31-b075-45e1-912e-0b664b555766)
