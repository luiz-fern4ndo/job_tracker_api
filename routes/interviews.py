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


# TODO: Criar uma entrevista ligada a uma candidatura e executar,
# acho que o erro está na linha 34, quando cria a entrevista
