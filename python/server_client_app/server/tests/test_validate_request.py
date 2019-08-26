import pytest
from datetime import datetime

from protocol import validate_request


@pytest.fixture
def initial_action():
    return 'test'


@pytest.fixture
def expected_response():
    return True


@pytest.fixture
def initial_request(initial_action):
    return {
        'action': initial_action,
        'timestamp': datetime.now().timestamp()
    }


def test_validate_request(initial_request, expected_response):
    actual_response = validate_request(initial_request)
    assert actual_response == expected_response
