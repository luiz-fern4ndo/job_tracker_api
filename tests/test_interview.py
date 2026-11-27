from http import HTTPStatus


def test_create_interview(client, application):
    response = client.post(
        '/interviews/',
        json={
            "application_id": application['id'],
            "interview_date": "2026-11-25T22:28:40.167Z",
            "feedback": "string",
            "next_steps": "string",
            "stage": "rh",
            "language": "pt",
            "result": "in_progress"
        }
    )

    assert response.status_code == HTTPStatus.CREATED
    assert 'id' in response.json()


def test_read_all_interviews(client, application, interview):
    response = client.get('/interviews/')

    assert response.status_code == HTTPStatus.OK
    assert response.json()[0]['application_id'] == application['id']


def test_read_interview_with_id(client, interview):
    response = client.get(f'/interviews/{interview["id"]}')

    assert response.status_code == HTTPStatus.OK
    assert response.json()['id'] == interview['id']


def test_read_interview_with_id_not_found(client, interview):

    response = client.get('/interviews/10')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Interview not found'}
