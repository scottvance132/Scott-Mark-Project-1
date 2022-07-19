from flask import Blueprint, request, session
from model.user import User
from model.reimbursement import Reimbursement
from service.reimbursement_service import ReimbursementService
from exceptions.incorrect_user_error import IncorrectUserError

rc = Blueprint('reimbursement_controller', __name__)

reimbursement_service = ReimbursementService()


@rc.route("/users/<user_id>/reimbursements")   # GET /users/<user_id>
def get_all_reimb_by_user_id(user_id):
    args = request.args
    status = args.get('status')
    return {"reimbursements": reimbursement_service.get_all_reimb_by_user_id(user_id, status)}
    # try:
    #     if "employee" in session['user_info']['role']:
    #         return {
    #             "reimbursements": reimbursement_service.get_all_reimb_by_user_id(user_id, status)
    #         }
    #     else:
    #         return {
    #             "message": "Invalid user role"
    #         }, 400
    # except IncorrectUserError as e:
    #     return {
    #         "message": str(e)
    #     }
# "'{user_info': {'role': 'employee'}}"


@rc.route("/reimbursements")
def get_all_reimb():
    args = request.args
    status = args.get('status')
    if "finance_manager" in session['user_info']['role']:
        return {
            "reimbursements": reimbursement_service.get_all_reimb(status)
        }
    else:
        return {
            "message": "Invalid user role"
        }, 400


@rc.route('/users/<user_id>/reimbursements', methods=['POST'])
def add_reimb_by_author(user_id):
    reimb_json_dict = request.get_json()
    reimb_obj = Reimbursement(None, reimb_json_dict['reimbursement_amount'], None, None, None, reimb_json_dict['type'],
                              reimb_json_dict['description'], None, reimb_json_dict['author'], None)
    return reimbursement_service.add_reimbursement_by_user_id(reimb_obj), 201


@rc.route('/reimbursements/<reimbursement_id>', methods=['PUT'])
def update_reimbursement(reimbursement_id):
    reimb_json_dict = request.get_json()
    return reimbursement_service.update_reimbursement(Reimbursement(reimbursement_id, None, None,
                                                                    None,
                                                                    reimb_json_dict['status'], None, None, None, None,
                                                                    session['user_info']['user_id']))
