import psycopg
from model.reimbursement import Reimbursement


class ReimbursementDao:

    def get_all_reimb_by_user_id(self,reimb_author):
        with psycopg.connect(host="127.0.0.1", port='5432', dbname="prj1", user="postgres",
                             password='mAshgAey208') as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM reimbursements WHERE reimb_author = %s", (reimb_author,))

                my_list_of_reimbursement_objs = []

                for reimb in cur:
                    open('frontend/receipts/' + str(reimb[0]) + '.jpeg', 'wb').write(reimb[7])
                    reimb_id = reimb[0]
                    amount = reimb[1]
                    submitted = reimb[2]
                    resolved = reimb[3]
                    status = reimb[4]
                    type = reimb[5]
                    description = reimb[6]
                    receipt = '/receipts/' + str(reimb[0]) + '.jpeg'
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
                    open('frontend/receipts/' + str(reimb[0]) + '.jpeg', 'wb').write(reimb[7])
                    reimb_id = reimb[0]
                    amount = reimb[1]
                    submitted = reimb[2]
                    resolved = reimb[3]
                    status = reimb[4]
                    type = reimb[5]
                    description = reimb[6]
                    receipt = '/receipts/' + str(reimb[0]) + '.jpeg'
                    author = reimb[8]
                    resolver = reimb[9]

                    my_reimb_obj = Reimbursement(reimb_id, amount, submitted, resolved, status, type, description,
                                                 receipt, author, resolver)
                    my_list_of_reimbursement_objs_p.append(my_reimb_obj)

                return my_list_of_reimbursement_objs_p

    def get_all_reimb(self):
        with psycopg.connect(host="127.0.0.1", port='5432', dbname="prj1", user="postgres",
                             password='mAshgAey208') as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM reimbursements")

                my_list_of_reimbursement_objs = []

                for reimb in cur:
                    open('frontend/receipts/' + str(reimb[0]) + '.jpeg', 'wb').write(reimb[7])
                    reimb_id = reimb[0]
                    amount = reimb[1]
                    submitted = reimb[2]
                    resolved = reimb[3]
                    status = reimb[4]
                    type = reimb[5]
                    description = reimb[6]
                    receipt = '/receipts/' + str(reimb[0]) + '.jpeg'
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
                    open('frontend/receipts/' + str(reimb[0]) + '.jpeg', 'wb').write(reimb[7])
                    reimb_id = reimb[0]
                    amount = reimb[1]
                    submitted = reimb[2]
                    resolved = reimb[3]
                    status = reimb[4]
                    type = reimb[5]
                    description = reimb[6]
                    receipt = '/receipts/' + str(reimb[0]) + '.jpeg'
                    author = reimb[8]
                    resolver = reimb[9]

                    my_reimb_obj = Reimbursement(reimb_id, amount, submitted, resolved, status, type, description,
                                                 receipt, author, resolver)
                    my_list_of_reimbursement_objs.append(my_reimb_obj)

                return my_list_of_reimbursement_objs

    def add_reimbursement_by_user_id(self, reimb_obj, receipt):
        file = receipt.read()
        amount_add = reimb_obj.amount
        type_add = reimb_obj.type
        desc_add = reimb_obj.desc
        author_add = reimb_obj.author
        with psycopg.connect(host="127.0.0.1", port='5432', dbname="prj1", user="postgres",
                             password='mAshgAey208') as conn:
            with conn.cursor() as cur:

                cur.execute('INSERT INTO reimbursements (reimbursement_amount, reimb_type, description, receipt, '
                            'reimb_author) VALUES (%s, %s, %s, %s, %s) RETURNING *',
                            (amount_add, type_add, desc_add, file, author_add))

                inserted_reimb_row = cur.fetchone()

                conn.commit()

                return Reimbursement(inserted_reimb_row[0], inserted_reimb_row[1], inserted_reimb_row[2],
                                     inserted_reimb_row[3], inserted_reimb_row[4], inserted_reimb_row[5],
                                     inserted_reimb_row[6], None, inserted_reimb_row[8],
                                     inserted_reimb_row[9])

    def update_reimb(self, reimb_obj):
        with psycopg.connect(host="127.0.0.1", port='5432', dbname="prj1", user="postgres",
                             password='mAshgAey208') as conn:
            with conn.cursor() as cur:
                cur.execute('UPDATE reimbursements SET status = %s, reimb_resolver = %s, resolved = CURRENT_TIMESTAMP'
                            ' WHERE reimb_id = %s RETURNING *',
                            (reimb_obj.status, reimb_obj.resolver, reimb_obj.reimb_id))

                conn.commit()

                print(cur.statusmessage)

                updated_reimb_row = cur.fetchone()
                if updated_reimb_row is None:
                    return None

                return Reimbursement(updated_reimb_row[0], updated_reimb_row[1], updated_reimb_row[2],
                                     updated_reimb_row[3], updated_reimb_row[4], updated_reimb_row[5],
                                     updated_reimb_row[6], updated_reimb_row[7], updated_reimb_row[8],
                                     updated_reimb_row[9])

