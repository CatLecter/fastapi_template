from datetime import datetime

from sqlalchemy import TIMESTAMP, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    type_annotation_map = {
        datetime: TIMESTAMP(timezone=False),
    }

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.current_timestamp())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.current_timestamp(), onupdate=func.current_timestamp()
    )

    def to_dict(self, exclude: set[str] | None = None) -> dict:
        delattr(self, '_sa_instance_state')
        if exclude:
            for field in exclude:
                delattr(self, field)
        return self.__dict__
