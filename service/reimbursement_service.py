from dao.reimbursement_dao import ReimbursementDao

class ReimbursementService:

    def __init__(self):
        self.reimbursement_dao = ReimbursementDao()

    def get_all_reimb_by_user_id(self, user_id, query_1):
        if query_1 is None:
            return list(map(lambda x: x.to_dict(), self.reimbursement_dao.get_all_reimb_by_user_id(user_id)))

        if query_1 is not None:
            return list(map(lambda x: x.to_dict(), self.reimbursement_dao.get_all_reimb_by_user_id_status(user_id,
                                                                                                           query_1)))
        # if query_2 is not None:
        #     return list(map(lambda x: x.to_dict(), self.reimbursement_dao.get_all_reimb_by_user_id_approved(user_id,
        #                                                                                                     query_2)))
        # if query_3 is not None:
        #     return list(map(lambda x: x.to_dict(), self.reimbursement_dao.get_all_reimb_by_user_id_denied(user_id,
        #                                                                                                   query_3)))
        else:
            return []

    def get_all_reimb(self, query_1):
        if query_1 is None:
            return list(map(lambda x: x.to_dict(), self.reimbursement_dao.get_all_reimb()))

        if query_1 is not None:
            return list(map(lambda x: x.to_dict(), self.reimbursement_dao.get_all_reimb_status(query_1)))

    def add_reimbursement_by_user_id(self, reimb_obj):
        return self.reimbursement_dao.add_reimbursement_by_user_id(reimb_obj).to_dict()


