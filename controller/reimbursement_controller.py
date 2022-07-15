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


@rc.route('/users/<user_id>/reimbursements', methods=['POST'])
def add_reimb_by_author(user_id):
    reimb_json_dict = request.get_json()
    reimb_obj = Reimbursement(None, reimb_json_dict['reimbursement_amount'], None, None, None, reimb_json_dict['type'],
                              reimb_json_dict['description'], None, reimb_json_dict['author'], None)
    return reimbursement_service.add_reimbursement_by_user_id(reimb_obj), 201
