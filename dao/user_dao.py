import psycopg
from model.user import User


class UserDao:

    def get_all_users(self):
        with psycopg.connect(host="127.0.0.1", port='5432', dbname="prj1", user="postgres",
                             password='mAshgAey208') as conn:
            with conn.cursor() as cur:

                cur.execute('SELECT * FROM users')

                my_list_of_user_objs = []
                for user in cur:
                    user_id = user[0]
                    username = user[1]
                    password = user[2]
                    first_name = user[3]
                    last_name = user[4]
                    email = user[5]
                    role = user[6]

                    my_user_obj = User(user_id, username, password, first_name, last_name, email, role)
                    my_list_of_user_objs.append(my_user_obj)

                print(my_list_of_user_objs)
                return my_list_of_user_objs

    def get_user_by_id(self, id):
        with psycopg.connect(host="127.0.0.1", port='5432', dbname="prj1", user="postgres",
                             password='mAshgAey208') as conn:
            with conn.cursor() as cur:

                cur.execute('SELECT * FROM users WHERE id = %s', (id,))

                c_row = cur.fetchone()
                if not c_row:
                    return None

                user_id = c_row[0]
                username = c_row[1]
                password = c_row[2]
                first_name = c_row[3]
                last_name = c_row[4]
                email = c_row[5]
                role = c_row[6]

                return User(user_id, username, password, first_name, last_name, email, role)
