from flask import session
from dao.reimbursement_dao import ReimbursementDao
from exceptions.incorrect_user_error import IncorrectUserError
from model.user import User
from dao.user_dao import UserDao


class ReimbursementService:

    def __init__(self):
        self.reimbursement_dao = ReimbursementDao()
        self.user_dao = UserDao()

    def get_all_reimb_by_user_id(self, user_id, query_1):
        list_of_reimb = self.reimbursement_dao.get_all_reimb_by_user_id(user_id)

        if query_1 is None:
            return list(map(lambda x: x.to_dict(), self.reimbursement_dao.get_all_reimb_by_user_id(user_id)))

        # if query_1 in ('pending', 'approved', 'denied')
        if query_1 is not None:
            return list(map(lambda x: x.to_dict(), self.reimbursement_dao.get_all_reimb_by_user_id_status(user_id,
                                                                                                          query_1)))

    def get_all_reimb(self, query_1):
        if query_1 is None:
            return list(map(lambda x: x.to_dict(), self.reimbursement_dao.get_all_reimb()))

        if query_1 is not None:
            return list(map(lambda x: x.to_dict(), self.reimbursement_dao.get_all_reimb_status(query_1)))

    def add_reimbursement_by_user_id(self, reimb_obj):
        return self.reimbursement_dao.add_reimbursement_by_user_id(reimb_obj).to_dict()

    def update_reimbursement(self, reimb_obj):
        # if self.reimbursement_dao.update_reimb(reimb_obj) is None:
        return self.reimbursement_dao.update_reimb(reimb_obj).to_dict()


