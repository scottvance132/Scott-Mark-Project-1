from flask import Blueprint, request
from model.user import User
from model.reimbursement import Reimbursement
from service.reimbursement_service import ReimbursementService

rc = Blueprint('reimbursement_controller', __name__)

reimbursement_service = ReimbursementService()

@rc.route("/users/<user_id>/reimbursements")   # GET /users/<user_id>
def get_all_reimb_by_user_id(user_id):

    return {
        "reimbursements": reimbursement_service.get_all_reimb_by_user_id(user_id)
    }

@rc.route("/reimbursements")
def get_all_reimb():

    return {
        "reimbursements": reimbursement_service.get_all_reimb()
    }