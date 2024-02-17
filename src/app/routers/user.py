from fastapi import APIRouter, Depends

from app.dependencies import get_user_service
from app.schemes.external import UserRequest
from app.schemes.internal import InternalUserRequest, InternalUserResponse
from app.services import UserService

router = APIRouter(prefix='/user', tags=['Users'])


@router.post(path='/', response_model=InternalUserResponse)
async def add_ticket(
    item: UserRequest,
    user_service: UserService = Depends(get_user_service),
) -> InternalUserResponse:
    return await user_service.add_user(InternalUserRequest(**item.model_dump()))
