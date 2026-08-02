from config.database import Database
from auth.authService import AuthService
from model.user import User

class UserRepository:

    def create_user(self, user: User) -> dict:
        hashed_pwd = AuthService.hash_password(user.password)

        query = """
        INSERT INTO users (full_name, email, password, phone, gender, date_of_birth, country)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        try:
            with Database.get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, (
                        user.full_name,
                        user.email,
                        hashed_pwd,
                        user.phone,
                        user.gender,
                        user.date_of_birth,
                        user.country
                    ))
                conn.commit()
                return {
                    "status": "success",
                    "full_name": user.full_name
                }
        except Exception as e:
            return {
                "status": "error",
                "message": f"فشل إنشاء الحساب: {str(e)}"
            }

    def login_user(self, input_email: str, input_password: str) -> dict:
        
        query = "SELECT full_name, password FROM users WHERE email = %s;"
        
        try:
            with Database.get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, (input_email,))
                    user_data = cursor.fetchone()
            if not user_data:
                return {
                    "status": "error",
                    "message": "Invalid email or password"
                }

            db_full_name, db_hashed_password = user_data

            if AuthService.verify_password(input_password, db_hashed_password):
                return {
                    "status": "success",
                    "full_name": db_full_name
                }
            else:
                return {
                    "status": "error",
                    "message": "Invalid email or password"
                }

        except Exception as e:
            return {
                "status": "error",
                "message": f"A system error occurred: {str(e)}"
            }