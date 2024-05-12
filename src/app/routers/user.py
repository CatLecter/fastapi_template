from uuid import UUID

from fastapi import APIRouter, Depends

from app.dependencies import get_user_service
from app.schemes.external import RequestUser, ResponseBriefUser, ResponseUser
from app.services import UserService

router = APIRouter(prefix='/user', tags=['Users'])


@router.post(path='/', response_model=ResponseUser)
async def add_user(item: RequestUser, user_service: UserService = Depends(get_user_service)) -> ResponseUser:
    return await user_service.add(item.to_internal())


@router.get('/', response_model=ResponseUser)
async def get_user_by_id(user_id: UUID, user_service: UserService = Depends(get_user_service)) -> ResponseUser:
    return await user_service.get_by_id(user_id)


@router.get('/list/', response_model=list[ResponseBriefUser])
async def get_all_users(user_service: UserService = Depends(get_user_service)) -> list[ResponseBriefUser]:
    return await user_service.get_all()
