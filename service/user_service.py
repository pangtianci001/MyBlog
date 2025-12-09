from db import get_conn
from entity.user import User

class UserService:
    def create_user(self, user):
        conn = get_conn()
        cursor = conn.cursor()

        sql = """
        INSERT INTO users (username, email, password)
        VALUES (%s, %s, %s)
        """

        cursor.execute(sql, (user.get_username(), user.get_email(), user.get_password()))
        conn.commit()

        user.set_id(cursor.lastrowid)

        cursor.close()
        conn.close()

        return user
    
    def get_user(self, user_id):
        conn = get_conn()
        cursor = conn.cursor(dictionary=True)

        sql = """
        SELECT *
        FROM users
        WHERE id=%s
        """

        cursor.execute(sql, (user_id,))
        row = cursor.fetchone()

        cursor.close()
        conn.close()

        if not row:
            return None
        
        user = User(
            username=row["username"],
            email=row["email"],
            password=row["password"]
        )

        user.set_id(row["id"])

        return user