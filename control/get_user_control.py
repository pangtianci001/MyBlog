from service.user_service import UserService

class GetUserControl:
    def execute(self, user_id):
        user_service = UserService()
        return user_service.get_user(user_id)