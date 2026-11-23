import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from database import get_session
from main import app
from models.base import table_registry


@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    with Session(engine) as session:
        table_registry.metadata.create_all(engine)
        yield session
        table_registry.metadata.drop_all(engine)


@pytest.fixture
def client(session):
    def override_get_session():
        yield session

    app.dependency_overrides[get_session] = override_get_session
    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def application(client):
    response = client.post(
        '/applications/',
        json={
            'company': 'Secret',
            'job_title': 'Desenvolvedor Backend Python',
            'source': 'Linkedin',
            'technologies': [
                'Python',
                'FastAPI',
                'Django',
                'PostgreSQL',
                'Docker',
            ],
            'response_timeframe_days': 7,
            'salary_range': 'a combinar',
            'next_step': '',
            'notes': '',
            'work_model': 'remote',
            'resume_used': 'pt',
            'status': 'applied',
        },
    )

    return response.json()
