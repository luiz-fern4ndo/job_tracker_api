from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_session
from models.application import Application
from schemas.application import ApplicationCreate, ApplicationRead

router = APIRouter()


@router.post(
    '/applications/',
    response_model=ApplicationRead,
    status_code=HTTPStatus.CREATED,
)
def application_create(
    application: ApplicationCreate, session: Session = Depends(get_session)
):
    application_new = Application(**application.model_dump())

    session.add(application_new)
    session.commit()
    session.refresh(application_new)

    return application_new


@router.get(
        '/applications/',
        status_code=HTTPStatus.OK,
        response_model=list[ApplicationRead]
)
def application_read(session: Session = Depends(get_session)):
    applications = session.scalars(select(Application)).all()

    return applications
