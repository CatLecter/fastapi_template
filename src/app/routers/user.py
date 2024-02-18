from uuid import UUID

from fastapi import APIRouter, Depends

from app.dependencies import get_user_service
from app.schemes.external import UserRequest
from app.schemes.internal import InternalBriefUserResponse
from app.schemes.internal import InternalUserRequest, InternalUserResponse
from app.services import UserService

router = APIRouter(prefix='/user', tags=['Users'])


@router.post(path='/', response_model=InternalUserResponse)
async def add_ticket(
    item: UserRequest,
    user_service: UserService = Depends(get_user_service),
) -> InternalUserResponse:
    return await user_service.add_user(InternalUserRequest(**item.model_dump()))


@router.get('/list/', response_model=list[InternalBriefUserResponse])
async def get_users(
    user_service: UserService = Depends(get_user_service),
) -> list[InternalBriefUserResponse]:
    return await user_service.get_users()


@router.get('/', response_model=InternalUserResponse)
async def get_user(
    user_id: UUID,
    user_service: UserService = Depends(get_user_service),
) -> InternalUserResponse:
    return await user_service.get_user(user_id)
