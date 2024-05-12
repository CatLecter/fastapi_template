from dataclasses import dataclass


@dataclass
class InternalRequestUser:
    __slots__ = ['full_name', 'mobile_phone']
    full_name: str
    mobile_phone: str
