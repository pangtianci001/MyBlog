from entity.user import User
from service.user_service import UserService

class CreateUserControl:
    def execute(self, username, email, password):
        user = User(username, email, password)
        user_service = UserService()
        user = user_service.create_user(user)
        return user