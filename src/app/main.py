from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from app.dependencies import init_dependencies
from app.routers import router
from app.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa
    init_dependencies()
    yield


app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION,
    docs_url=settings.DOC_URL,
    openapi_url=settings.OPENAPI_URL,
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host=settings.SERVER_HOST,
        port=int(settings.SERVER_PORT),
        log_level=settings.LOG_LEVEL,
        reload=settings.DEVELOP,
    )
