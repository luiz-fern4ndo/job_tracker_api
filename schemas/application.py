from datetime import datetime

from pydantic import BaseModel, ConfigDict

from models.enums import (
    ApplicationStatus,
    CurriculumUsedStatus,
    WorkModelStatus,
)
from schemas.interview import InterviewRead


class ApplicationCreate(BaseModel):
    company: str
    job_title: str
    source: str
    technologies: list[str]
    response_timeframe_days: int | None
    salary_range: str | None
    next_step: str | None
    notes: str | None
    work_model: WorkModelStatus = WorkModelStatus.IN_PERSON
    resume_used: CurriculumUsedStatus = CurriculumUsedStatus.PT
    status: ApplicationStatus = ApplicationStatus.APPLIED


class ApplicationRead(BaseModel):
    id: int
    company: str
    job_title: str
    application_date: datetime
    source: str
    technologies: list[str]
    response_timeframe_days: int | None
    salary_range: str | None
    next_step: str | None
    notes: str | None
    work_model: WorkModelStatus
    resume_used: CurriculumUsedStatus
    status: ApplicationStatus

    model_config = ConfigDict(from_attributes=True)


class ApplicationReadWithInterviews(ApplicationRead):
    interviews: list[InterviewRead]
