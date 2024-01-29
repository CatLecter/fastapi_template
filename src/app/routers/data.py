from fastapi import APIRouter, Depends

from app.dependencies import get_data_service
from app.schemes.external import DataRequest
from app.schemes.internal import InternalDataRequest, InternalDataResponse
from app.services import DataService

router = APIRouter(prefix='/data', tags=['Data'])


@router.post(path='/', response_model=InternalDataResponse)
async def add_data(item: DataRequest, data_service: DataService = Depends(get_data_service)) -> InternalDataResponse:
    return await data_service.add_data(InternalDataRequest(**item.model_dump()))
