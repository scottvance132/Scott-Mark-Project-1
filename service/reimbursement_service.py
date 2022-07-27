from dao.reimbursement_dao import ReimbursementDao
from dao.user_dao import UserDao
from exceptions.invalid_parameter_error import InvalidParameterError


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

    def add_reimbursement_by_user_id(self, reimb_obj, receipt):
        if reimb_obj.amount is None:
            raise InvalidParameterError(f"The reimbursement amount must not be blank!")
        if not str(reimb_obj.amount).isnumeric():
            raise InvalidParameterError(f"The reimbursement amount must be an integer!")
        if reimb_obj.desc is '':
            raise InvalidParameterError(f"The reimbursement description must not be blank!")
        if reimb_obj.receipt is None:
            raise InvalidParameterError(f"The reimbursement receipt must not be blank!")
        if reimb_obj.type is None:
            raise InvalidParameterError(f"The reimbursement type must not be blank!")
        else:
            return self.reimbursement_dao.add_reimbursement_by_user_id(reimb_obj, receipt).to_dict()

    def update_reimbursement(self, reimb_obj):
        # if self.reimbursement_dao.update_reimb(reimb_obj) is None:
        return self.reimbursement_dao.update_reimb(reimb_obj).to_dict()


