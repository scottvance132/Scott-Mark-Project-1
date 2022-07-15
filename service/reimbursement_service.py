from dao.reimbursement_dao import ReimbursementDao

class ReimbursementService:

    def __init__(self):
        self.reimbursement_dao = ReimbursementDao()

    def get_all_reimb_by_user_id(self, user_id):
        list_of_reimbursement_objects = self.reimbursement_dao.get_all_reimb_by_user_id(user_id)

        return list(map(lambda x: x.to_dict(), list_of_reimbursement_objects))

    def get_all_reimb(self):
        list_of_reimbursement_objects = self.reimbursement_dao.get_all_reimb()

        return list(map(lambda x: x.to_dict(), list_of_reimbursement_objects))


