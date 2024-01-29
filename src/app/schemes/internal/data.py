from dataclasses import dataclass
from uuid import UUID


@dataclass
class InternalDataRequest:
    __slots__ = ['a', 'b', 'c', 'd', 'e', 'f', 'ts']
    a: int | None
    b: int | None
    c: int | None
    d: int | None
    e: int | None
    f: int | None
    ts: int


@dataclass
class InternalDataResponse(InternalDataRequest):
    __slots__ = ['data_uuid']
    data_uuid: UUID
