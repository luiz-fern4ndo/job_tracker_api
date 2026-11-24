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
    assert 'id' in response.json()


def test_read_with_id(client, application):

    response = client.get(f'/applications/{application["id"]}')

    assert response.status_code == HTTPStatus.OK
    assert response.json()['id'] == application['id']


def test_read_application(client, application):

    response = client.get('/applications/')

    assert response.status_code == HTTPStatus.OK
    assert any(
        application['id'] == application['id']
        for application in response.json()
    )


def test_delete_application(client, application):

    response = client.delete(f'/applications/{application["id"]}')

    assert response.status_code == HTTPStatus.NO_CONTENT

    response_get = client.get(f'/applications/{application["id"]}')
    assert response_get.status_code == HTTPStatus.NOT_FOUND


def test_update_application(client, application):

    response = client.patch(
        f'/applications/{application["id"]}',
        json={'company': 'Nova Empresa'}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json()['company'] == 'Nova Empresa'
    assert response.json()['job_title'] == application['job_title']
