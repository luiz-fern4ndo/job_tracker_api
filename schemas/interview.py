from datetime import datetime

from pydantic import BaseModel, ConfigDict

from models.enums import (
    InterviewResultStatus,
    InterviewStageStatus,
    LanguageStatus,
)
from schemas.common import ApplicationSummary


class InterviewCreate(BaseModel):
    application_id: int
    interview_date: datetime
    feedback: str | None
    next_steps: str | None
    stage: InterviewStageStatus = InterviewStageStatus.RH
    language: LanguageStatus = LanguageStatus.PT
    result: InterviewResultStatus = InterviewResultStatus.IN_PROGRESS


class InterviewRead(BaseModel):
    id: int
    application_id: int
    interview_date: datetime
    feedback: str | None
    next_steps: str | None
    stage: InterviewStageStatus
    language: LanguageStatus
    result: InterviewResultStatus

    model_config = ConfigDict(from_attributes=True)


class InterviewReadWithApplication(InterviewRead):
    application: ApplicationSummary
