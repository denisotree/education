import pytest

from datetime import datetime
from echo.controllers import echo_controller


@pytest.fixture
def initial_action():
    return 'test'


@pytest.fixture()
def initial_code():
    return 200


@pytest.fixture
def initial_data():
    return "Hey world"


@pytest.fixture
def initial_request(initial_action, initial_data):
    return {
        'action': initial_action,
        'timestamp': datetime.now().timestamp(),
        'data': initial_data
    }


@pytest.fixture
def expected_action(initial_action):
    return initial_action


@pytest.fixture
def expected_code(initial_code):
    return initial_code


@pytest.fixture
def expected_data(initial_data):
    return initial_data


def test_action_echo_controller(initial_request, expected_action):
    actual_response = echo_controller(initial_request)
    assert actual_response.get('action') == expected_action


def test_code_echo_controller(initial_request, expected_code):
    actual_response = echo_controller(initial_request)
    assert actual_response.get('code') == expected_code


def test_data_echo_controller(initial_request, expected_data):
    actual_response = echo_controller(initial_request)
    assert actual_response.get('data') == expected_data
