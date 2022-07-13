from dao.user_dao import UserDao


class UserService:

    def __init__(self):
        self.user_dao = UserDao()

    def get_all_users(self):
        list_of_user_objects = self.user_dao.get_all_users()

        return list(map(lambda x: x.to_dict(), list_of_user_objects))
