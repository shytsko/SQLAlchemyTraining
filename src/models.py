from datetime import datetime

from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func, String, ForeignKey, text
from enum import StrEnum, auto


class Department(Base):
    __tablename__ = "department"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    workplaces: Mapped[list["Workplace"]] = relationship(back_populates="department")


class WorkplaceType(StrEnum):
    SUPERVISOR = "Руководитель"
    SPECIALIST = "Специалист"
    WORKER = "Рабочий"


class Workplace(Base):
    __tablename__ = "workplace"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256))
    workplace_type: Mapped[WorkplaceType]
    quantity: Mapped[int] = mapped_column(server_default=text('1'))
    department_id: Mapped[int] = mapped_column(ForeignKey("department.id", ondelete="CASCADE"))
    department: Mapped["Department"] = relationship(back_populates="workplaces")
