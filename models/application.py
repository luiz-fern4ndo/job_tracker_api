from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import JSON, Enum
from sqlalchemy.orm import (
    Mapped,
    mapped_as_dataclass,
    mapped_column,
    relationship,
)
from sqlalchemy.sql import func

from models import enums
from models.base import table_registry

if TYPE_CHECKING:
    from models.interview import Interview


@mapped_as_dataclass(table_registry)
class Application:
    __tablename__ = 'applications'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    company: Mapped[str]
    job_title: Mapped[str]
    interviews: Mapped[list['Interview']] = relationship(
        back_populates='application',
        init=False
    )

    application_date: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    source: Mapped[str]
    technologies: Mapped[list[str]] = mapped_column(JSON)
    response_timeframe_days: Mapped[int | None]
    salary_range: Mapped[str | None]
    next_step: Mapped[str | None]
    notes: Mapped[str | None]
    work_model: Mapped[enums.WorkModelStatus | None] = mapped_column(
        Enum(
            enums.WorkModelStatus,
            name='work_model_status',
            native_enum=False,
        ),
        default=None,
    )
    resume_used: Mapped[enums.CurriculumUsedStatus] = mapped_column(
        Enum(
            enums.CurriculumUsedStatus, name='resume_used', native_enum=False
        ),
        default=enums.CurriculumUsedStatus.PT,
    )
    status: Mapped[enums.ApplicationStatus] = mapped_column(
        Enum(
            enums.ApplicationStatus,
            name='status',
            native_enum=False,
        ),
        default=enums.ApplicationStatus.APPLIED,
    )
