import uuid
from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import INTEGER, MONEY, TEXT, UUID, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Ticket(Base):
    __tablename__ = 'tickets'  # noqa

    ticket_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    buyer_mobile_phone: Mapped[VARCHAR] = mapped_column(String(20), nullable=False)
    visitor_mobile_phone: Mapped[VARCHAR] = mapped_column(String(20), nullable=False)
    visitor_full_name: Mapped[TEXT] = mapped_column(String, nullable=False)
    event_name: Mapped[TEXT] = mapped_column(String, nullable=False)
    event_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    sector_number: Mapped[INTEGER] = mapped_column(Integer, nullable=False)
    row_number: Mapped[INTEGER] = mapped_column(Integer, nullable=False)
    place_number: Mapped[INTEGER] = mapped_column(Integer, nullable=False)
    ticket_price: Mapped[MONEY] = mapped_column(Float, nullable=False)
    status: Mapped[VARCHAR] = mapped_column(String(20), nullable=False)
