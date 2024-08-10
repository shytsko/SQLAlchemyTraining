from datetime import datetime

from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func


class FirstModel(Base):
    __tablename__ = "first"

    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[str]
    create_date: Mapped[datetime] = mapped_column(server_default=func.now())
