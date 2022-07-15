from dao.user_dao import UserDao


class UserService:

    def __init__(self):
        self.user_dao = UserDao()

    def get_all_users(self):
        list_of_user_objects = self.user_dao.get_all_users()

        return list(map(lambda x: x.to_dict(), list_of_user_objects))

    def get_user_by_user_id(self, user_id):
        user_obj = self.user_dao.get_user_by_id(user_id)
        return user_obj.to_dict()
