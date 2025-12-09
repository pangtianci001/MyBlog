class User:
    def __init__(self, username, email, password):
        self._id = None
        self._username = username
        self._email = email
        self._password = password

    def get_id(self):
        return self._id

    def get_username(self):
        return self._username
    
    def get_email(self):
        return self._email
    
    def get_password(self):
        return self._password
    
    def set_id(self, new_id):
        self._id = new_id

    def set_name(self, new_username):
        self._username = new_username
    
    def set_email(self, new_email):
        self._email = new_email
    
    def set_password(self, new_password):
        self._password = new_password

    def __repr__(self):
        return (
            f"Username: {self._username}\n"
            f"Email: {self._email}"
        )
    
if __name__ == "__main__":
    user1 = User("John", "john@gmail.com", "1234", "1 Jan 2000")
    print(user1)