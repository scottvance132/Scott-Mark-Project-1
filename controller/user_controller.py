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
