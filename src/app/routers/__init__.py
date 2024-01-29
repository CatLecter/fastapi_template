from fastapi import APIRouter

from app.routers.data import router as data_router
from app.settings import settings

router = APIRouter(prefix='/v1', include_in_schema=settings.DEVELOP)

router.include_router(data_router)
