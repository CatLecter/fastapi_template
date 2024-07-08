import uuid

from sqlalchemy import Index, String
from sqlalchemy.dialects.postgresql import TEXT, UUID, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class User(Base):
    __tablename__ = 'users'  # noqa
    __table_args__ = (Index('idx_user_mobile_phone', 'mobile_phone', unique=True),)
    user_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name: Mapped[TEXT] = mapped_column(String, nullable=False)
    mobile_phone: Mapped[VARCHAR] = mapped_column(String(20), nullable=False, unique=True)
