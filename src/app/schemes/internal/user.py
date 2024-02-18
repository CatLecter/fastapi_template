from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class InternalUserRequest:
    __slots__ = ['full_name', 'mobile_phone']
    full_name: str
    mobile_phone: str


@dataclass
class InternalUserResponse(InternalUserRequest):
    __slots__ = ['user_id', 'created_at', 'updated_at']
    user_id: UUID
    created_at: datetime
    updated_at: datetime


@dataclass
class InternalBriefUserResponse:
    __slots__ = ['user_id', 'full_name']
    user_id: UUID
    full_name: str
