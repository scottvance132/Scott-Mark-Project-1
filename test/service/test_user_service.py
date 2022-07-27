from exceptions.invalid_parameter_error import InvalidParameterError
from service.user_service import UserService
from model.user import User
from exceptions.user_not_found_error import UserNotFoundError
import pytest


def test_login_positive(mocker):
    # Arrange
    def mock_get_user_by_username(self, username):
        if username == 'joebob':
            return User(1, 'joebob', '$2b$12$S8F5dyJ1qrAjNpVaiLhmcuqDR0U1Ma9F/2oVdtJGEepO4w/wQ626u', 'Joe', 'Bob',
                        'joebob@email.com', 'employee')
        else:
            return UserNotFoundError

    mocker.patch('dao.user_dao.UserDao.get_user_by_username', mock_get_user_by_username)

    user_service = UserService()

    # Act
    actual = user_service.login('joebob', 'password')
    # Assert
    assert actual == {
        "user_id": 1,
        "username": 'joebob',
        'password': '$2b$12$S8F5dyJ1qrAjNpVaiLhmcuqDR0U1Ma9F/2oVdtJGEepO4w/wQ626u',
        'first_name': 'Joe',
        'last_name': 'Bob',
        'email': 'joebob@email.com',
        'role': 'employee'
    }


def test_login_negative_username(mocker):
    # Arrange
    def mock_get_user_by_username(self, username):
        if username == 'joebob':
            return User(1, 'joebob', '$2b$12$S8F5dyJ1qrAjNpVaiLhmcuqDR0U1Ma9F/2oVdtJGEepO4w/wQ626u', 'Joe', 'Bob',
                        'joebob@email.com', 'employee')
        else:
            return None

    mocker.patch('dao.user_dao.UserDao.get_user_by_username', mock_get_user_by_username)

    user_service = UserService()

    # Act
    with pytest.raises(InvalidParameterError) as excinfo:
        actual = user_service.login('joadfdbob', 'password1')

    assert str(excinfo.value) == "Invalid username and/or password"


def test_login_negative_password(mocker):
    # Arrange
    def mock_get_user_by_username(self, username):
        if username == 'joebob':
            return User(1, 'joebob', '$2b$12$S8F5dyJ1qrAjNpVaiLhmcuqDR0U1Ma9F/2oVdtJGEepO4w/wQ626u', 'Joe', 'Bob',
                        'joebob@email.com', 'employee')
        else:
            return InvalidParameterError

    mocker.patch('dao.user_dao.UserDao.get_user_by_username', mock_get_user_by_username)

    user_service = UserService()

    # Act
    with pytest.raises(InvalidParameterError) as excinfo:
        actual = user_service.login('joebob', 'password1')

    assert str(excinfo.value) == "Invalid username and/or password"


