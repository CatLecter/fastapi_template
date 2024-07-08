from fastapi import APIRouter

from src.routers.ticket import router as ticket_router
from src.routers.user import router as user_router
from src.settings import settings

router = APIRouter(prefix='/v1', include_in_schema=settings.DEVELOP)

router.include_router(ticket_router)
router.include_router(user_router)
