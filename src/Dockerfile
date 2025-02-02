FROM python:3.13-alpine3.21

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UV_SYSTEM_PYTHON 1
ENV UV_NO_CACHE True
ENV UV_PYTHON_DOWNLOADS never

WORKDIR /usr

RUN pip install --upgrade pip && \
    pip install uv

COPY ../pyproject.toml pyproject.toml
COPY ../uv.lock uv.lock

RUN uv pip install -r pyproject.toml

COPY ./src src

CMD gunicorn src.main:app \
    --workers ${WORKERS} \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000 \
    --log-level warning
