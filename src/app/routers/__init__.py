from fastapi import APIRouter

from app.routers.ticket import router as ticket_router
from app.routers.user import router as user_router
from app.settings import settings

router = APIRouter(prefix='/v1', include_in_schema=settings.DEVELOP)

router.include_router(ticket_router)
router.include_router(user_router)
