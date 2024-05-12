## FastAPI template

#### To run in a container:

1. Create a file with environment variables:

```shell
cp src/app/example.env src/app/.env
cp postgres/example.env postgres/.env
```

2. Run containers:

```shell
docker compose up -d --build
```

#### [Swagger](http://localhost:8000/docs)
