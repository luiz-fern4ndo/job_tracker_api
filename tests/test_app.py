from http import HTTPStatus


def test_create_application(client):

    response = client.post(
        '/applications/',
        json={
            'company': 'Globo',
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
    assert response.status_code == HTTPStatus.CREATED
    assert response.json()['id'] == 1
