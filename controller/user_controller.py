from flask import Blueprint, request, session

from exceptions.invalid_parameter_error import InvalidParameterError
from model.user import User
from service.user_service import UserService


uc = Blueprint('user_controller', __name__)
user_service = UserService()


@uc.route('/users')
def get_all_users():
    return {
        "users": user_service.get_all_users()
    }


@uc.route('/users/<user_id>')
def get_user_by_user_id(user_id):
    return {
        "user": user_service.get_user_by_user_id(user_id)
    }


@uc.route('/login', methods=['POST'])
def login():
    try:
        request_body_dict = request.get_json()

        username = request_body_dict['username']
        password = request_body_dict['password']

        user_dict = user_service.login(username, password)

        session['user_info'] = user_dict

        print(session)
        return user_dict, 200
    except InvalidParameterError as e:
        return {
            "message": str(e)
        }


@uc.route('/loginstatus', methods=['GET'])
def loginstatus():
    if session.get('user_info') is not None:
        return {
                   "message": "You are logged in",
                   "logged_in_user": session.get('user_info')
               }, 200
    else:
        return {
                   "message": "You are not logged in"
               }, 200


@uc.route('/logout', methods=['POST'])
def logout():
    session.clear()

    return {
        "message": "Successfully logged out"
    }, 200
