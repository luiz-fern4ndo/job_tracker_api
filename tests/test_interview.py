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
