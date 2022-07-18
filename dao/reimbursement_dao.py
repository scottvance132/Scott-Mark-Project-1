import psycopg
from model.reimbursement import Reimbursement
from model.user import User


class ReimbursementDao:

    def get_all_reimb_by_user_id(self,reimb_author):
        with psycopg.connect(host="127.0.0.1", port='5432', dbname="prj1", user="postgres",
                             password='mAshgAey208') as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM reimbursements WHERE reimb_author = %s", (reimb_author,))

                my_list_of_reimbursement_objs = []

                for reimb in cur:
                    reimb_id = reimb[0]
                    amount = reimb[1]
                    submitted = reimb[2]
                    resolved = reimb[3]
                    status = reimb[4]
                    type = reimb[5]
                    description = reimb[6]
                    receipt = reimb[7]
                    author = reimb[8]
                    resolver = reimb[9]

                    my_reimb_obj = Reimbursement(reimb_id, amount, submitted, resolved, status, type, description,
                                                 receipt, author, resolver)
                    my_list_of_reimbursement_objs.append(my_reimb_obj)

                return my_list_of_reimbursement_objs

    def get_all_reimb_by_user_id_status(self,reimb_author, query):
        with psycopg.connect(host="127.0.0.1", port='5432', dbname="prj1", user="postgres",
                             password='mAshgAey208') as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM reimbursements WHERE reimb_author = %s AND status = %s", (reimb_author,
                                                                                                     query))

                my_list_of_reimbursement_objs_p = []

                for reimb in cur:
                    reimb_id = reimb[0]
                    amount = reimb[1]
                    submitted = reimb[2]
                    resolved = reimb[3]
                    status = reimb[4]
                    type = reimb[5]
                    description = reimb[6]
                    receipt = reimb[7]
                    author = reimb[8]
                    resolver = reimb[9]

                    my_reimb_obj = Reimbursement(reimb_id, amount, submitted, resolved, status, type, description,
                                                 receipt, author, resolver)
                    my_list_of_reimbursement_objs_p.append(my_reimb_obj)

                return my_list_of_reimbursement_objs_p

    # def get_all_reimb_by_user_id_approved(self,reimb_author, query):
    #     with psycopg.connect(host="127.0.0.1", port='5432', dbname="prj1", user="postgres",
    #                          password='mAshgAey208') as conn:
    #         with conn.cursor() as cur:
    #             cur.execute("SELECT * FROM reimbursements WHERE reimb_author = %s AND status = %s", (reimb_author,
    #                                                                                                  query))
    #
    #             my_list_of_reimbursement_objs_a = []
    #
    #             for reimb in cur:
    #                 reimb_id = reimb[0]
    #                 amount = reimb[1]
    #                 submitted = reimb[2]
    #                 resolved = reimb[3]
    #                 status = reimb[4]
    #                 type = reimb[5]
    #                 description = reimb[6]
    #                 receipt = reimb[7]
    #                 author = reimb[8]
    #                 resolver = reimb[9]
    #
    #                 my_reimb_obj = Reimbursement(reimb_id, amount, submitted, resolved, status, type, description,
    #                                              receipt, author, resolver)
    #                 my_list_of_reimbursement_objs_a.append(my_reimb_obj)
    #
    #             return my_list_of_reimbursement_objs_a
    #
    # def get_all_reimb_by_user_id_denied(self,reimb_author, query):
    #     with psycopg.connect(host="127.0.0.1", port='5432', dbname="prj1", user="postgres",
    #                          password='mAshgAey208') as conn:
    #         with conn.cursor() as cur:
    #             cur.execute("SELECT * FROM reimbursements WHERE reimb_author = %s AND status = %s", (reimb_author,
    #                                                                                                  query))
    #
    #             my_list_of_reimbursement_objs_d = []
    #
    #             for reimb in cur:
    #                 reimb_id = reimb[0]
    #                 amount = reimb[1]
    #                 submitted = reimb[2]
    #                 resolved = reimb[3]
    #                 status = reimb[4]
    #                 type = reimb[5]
    #                 description = reimb[6]
    #                 receipt = reimb[7]
    #                 author = reimb[8]
    #                 resolver = reimb[9]
    #
    #                 my_reimb_obj = Reimbursement(reimb_id, amount, submitted, resolved, status, type, description,
    #                                              receipt, author, resolver)
    #                 my_list_of_reimbursement_objs_d.append(my_reimb_obj)
    #
    #             return my_list_of_reimbursement_objs_d

    def get_all_reimb(self):
        with psycopg.connect(host="127.0.0.1", port='5432', dbname="prj1", user="postgres",
                             password='mAshgAey208') as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM reimbursements")

                my_list_of_reimbursement_objs = []

                for reimb in cur:
                    reimb_id = reimb[0]
                    amount = reimb[1]
                    submitted = reimb[2]
                    resolved = reimb[3]
                    status = reimb[4]
                    type = reimb[5]
                    description = reimb[6]
                    receipt = reimb[7]
                    author = reimb[8]
                    resolver = reimb[9]

                    my_reimb_obj = Reimbursement(reimb_id, amount, submitted, resolved, status, type, description,
                                                 receipt, author, resolver)
                    my_list_of_reimbursement_objs.append(my_reimb_obj)

                return my_list_of_reimbursement_objs

    def get_all_reimb_status(self, query):
        with psycopg.connect(host="127.0.0.1", port='5432', dbname="prj1", user="postgres",
                             password='mAshgAey208') as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM reimbursements WHERE status = %s", (query,))

                my_list_of_reimbursement_objs = []

                for reimb in cur:
                    reimb_id = reimb[0]
                    amount = reimb[1]
                    submitted = reimb[2]
                    resolved = reimb[3]
                    status = reimb[4]
                    type = reimb[5]
                    description = reimb[6]
                    receipt = reimb[7]
                    author = reimb[8]
                    resolver = reimb[9]

                    my_reimb_obj = Reimbursement(reimb_id, amount, submitted, resolved, status, type, description,
                                                 receipt, author, resolver)
                    my_list_of_reimbursement_objs.append(my_reimb_obj)

                return my_list_of_reimbursement_objs

    def add_reimbursement_by_user_id(self, reimb_obj):
        amount_add = reimb_obj.amount
        type_add = reimb_obj.type
        desc_add = reimb_obj.desc
        author_add = reimb_obj.author
        with psycopg.connect(host="127.0.0.1", port='5432', dbname="prj1", user="postgres",
                             password='mAshgAey208') as conn:
            with conn.cursor() as cur:

                cur.execute('INSERT INTO reimbursements (reimbursement_amount, reimb_type, description, reimb_author) '
                            'VALUES (%s, %s, %s, %s) RETURNING *', (amount_add, type_add, desc_add, author_add,))

                inserted_reimb_row = cur.fetchone()

                conn.commit()

                return Reimbursement(inserted_reimb_row[0], inserted_reimb_row[1], inserted_reimb_row[2],
                                     inserted_reimb_row[3], inserted_reimb_row[4], inserted_reimb_row[5],
                                     inserted_reimb_row[6], inserted_reimb_row[7], inserted_reimb_row[8],
                                     inserted_reimb_row[9])

