from dataclasses import dataclass


@dataclass(slots=True)
class InternalRequestUser:
    full_name: str
    mobile_phone: str
