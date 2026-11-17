from enum import StrEnum


class ApplicationStatus(StrEnum):
    APPLIED = 'applied'
    SCREENING = 'screening'
    TECHNICAL_INTERVIEW = 'technical_interview'
    RH_INTERVIEW = 'rh_interview'
    OFFER = 'offer'
    REJECTED = 'rejected'
    GAVE_UP = 'gave_up'


class WorkModelStatus(StrEnum):
    REMOTE = 'remote'
    HYBRID = 'hybrid'
    IN_PERSON = 'in_person'


class LanguageStatus(StrEnum):
    PT = 'pt'
    EN = 'en'


class CurriculumUsedStatus(StrEnum):
    PT = 'pt'
    EN = 'en'


class InterviewStageStatus(StrEnum):
    RH = 'rh'
    TECHNICAL = 'technical'
    CULTURAL = 'cultural'
    FINAL = 'final'


class InterviewResultStatus(StrEnum):
    APPROVED = 'approved'
    FAILED = 'failed'
    IN_PROGRESS = 'in_progress'
    CANCELED = 'canceled'
