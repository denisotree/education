import pytest

from datetime import datetime
from serverdate.controllers import date_controller


@pytest.fixture
def initial_action():
    return 'test'


@pytest.fixture()
def initial_code():
    return 200


@pytest.fixture()
def initial_data():
    return datetime.now().timestamp()


@pytest.fixture
def initial_request(initial_action, initial_data):
    return {
        'action': initial_action,
        'timestamp': datetime.now().timestamp()
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


def test_action_date_controller(initial_request, expected_action):
    actual_response = date_controller(initial_request)
    assert actual_response.get('action') == expected_action


def test_code_date_controller(initial_request, expected_code):
    actual_response = date_controller(initial_request)
    assert actual_response.get('code') == expected_code


def test_data_date_controller(initial_request, expected_data):
    actual_response = date_controller(initial_request)
    assert actual_response.get('data') > expected_data
