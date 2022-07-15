from flask import Blueprint, request

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
