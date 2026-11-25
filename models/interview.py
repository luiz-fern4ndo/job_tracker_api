from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from application import Application

from datetime import datetime

from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import enums
from models.base import table_registry


@table_registry.mapped_as_dataclass
class Interview:
    __tablename__ = 'interviews'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    interview_date: Mapped[datetime]
    feedback: Mapped[str | None]
    next_steps: Mapped[str | None]
    application_id: Mapped[int] = mapped_column(ForeignKey('applications.id'))
    application: Mapped['Application'] = relationship(
        back_populates='interviews',
        init=False
    )
    stage: Mapped[enums.InterviewStageStatus] = mapped_column(
        Enum(
            enums.InterviewStageStatus,
            name='interview_status',
            native_enum=False,
        ),
        default=enums.InterviewStageStatus.RH,
    )
    language: Mapped[enums.LanguageStatus] = mapped_column(
        Enum(
            enums.LanguageStatus,
            name='language_status',
            native_enum=False,
        ),
        default=enums.LanguageStatus.PT,
    )
    result: Mapped[enums.InterviewResultStatus] = mapped_column(
        Enum(
            enums.InterviewResultStatus,
            name='interview_result_status',
            native_enum=False,
        ),
        default=enums.InterviewResultStatus.IN_PROGRESS,
    )
