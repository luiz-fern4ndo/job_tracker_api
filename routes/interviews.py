from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_session
from models.application import Application
from models.interview import Interview
from schemas.interview import InterviewCreate, InterviewRead

router = APIRouter()


@router.post(
    '/interviews/',
    status_code=HTTPStatus.CREATED,
    response_model=InterviewRead,
)
def create_interview(
    interview: InterviewCreate,
    session: Session = Depends(get_session),
):

    application_db = session.scalar(
        select(Application).where(Application.id == interview.application_id)
    )

    if not application_db:
        raise HTTPException(
            detail='Application not found', status_code=HTTPStatus.NOT_FOUND
        )

    interview = Interview(**interview.model_dump())
    session.add(interview)
    session.commit()
    session.refresh(interview)

    return interview


@router.get(
        '/interviews/',
        status_code=HTTPStatus.OK,
        response_model=list[InterviewRead]
)
def read_all_interviews(session: Session = Depends(get_session)):

    interview_db = session.scalars(select(Interview)).all()

    return interview_db


@router.get(
    '/interviews/{interview_id}',
    response_model=InterviewRead,
    status_code=HTTPStatus.OK
)
def read_interview_with_id(
    interview_id: int,
    session: Session = Depends(get_session)
):

    interview_db = session.scalar(
        select(Interview).where(Interview.id == interview_id)
    )

    if not interview_db:
        raise HTTPException(
            detail='Interview not found',
            status_code=HTTPStatus.NOT_FOUND
        )

    return interview_db
