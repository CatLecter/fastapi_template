FROM python:3.12.2-alpine3.19

EXPOSE 8000

WORKDIR /usr/src

COPY . ./app

RUN pip install -U pip && pip install --no-cache-dir -r app/requirements.txt

CMD gunicorn app.main:app \
    --workers ${WORKERS} \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000 \
    --log-level warning
