from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_session
from models.application import Application
from schemas.application import (
    ApplicationCreate,
    ApplicationRead,
    ApplicationUpdate
)

router = APIRouter()


@router.post(
    '/applications/',
    response_model=ApplicationRead,
    status_code=HTTPStatus.CREATED,
)
def create_application(
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
def read_application(session: Session = Depends(get_session)):
    applications = session.scalars(select(Application)).all()

    return applications


@router.get(
        '/applications/{application_id}',
        status_code=HTTPStatus.OK,
        response_model=ApplicationRead
)
def read_application_with_id(
    application_id: int, session: Session = Depends(get_session)):

    application_db = session.scalar(
        select(Application).where(Application.id == application_id)
    )

    if not application_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Application not found'
        )

    return application_db


@router.patch(
        '/applications/{application_id}',
        status_code=HTTPStatus.OK,
        response_model=ApplicationRead
)
def update_application(
    application: ApplicationUpdate,
    application_id: int,
    session: Session = Depends(get_session),
):
    application_db = session.scalar(
        select(Application).where(Application.id == application_id)
    )

    if not application_db:
        raise HTTPException(
            detail='Application not found',
            status_code=HTTPStatus.NOT_FOUND
        )

    for key, value in application.model_dump(exclude_unset=True).items():
        setattr(application_db, key, value)

    session.add(application_db)
    session.commit()
    session.refresh(application_db)

    return application_db


@router.delete(
        '/applications/{application_id}/',
        status_code=HTTPStatus.NO_CONTENT
)
def delete_application(
    application_id: int,
    session: Session = Depends(get_session)
):
    application = session.scalar(
        select(Application).where(Application.id == application_id)
    )

    if not application:
        raise HTTPException(
            detail='Application not found',
            status_code=HTTPStatus.NOT_FOUND
        )
    session.delete(application)
    session.commit()
