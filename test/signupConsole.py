import sys
import os

# Add project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.database import Database
from model.user import User
from repo.userRepo import UserRepository

# 1. Initialize Database Pool
Database.initialize()

repo = UserRepository()

# --- 2. Test Sign Up ---
print("--- Testing Sign Up ---")
new_user = User(
    full_name="Mohammad Lolah",
    email="mohammad@example.com",
    password="mySecretPassword123",
    phone="0790000000",
    gender="male",
    date_of_birth="2000-01-01",
    country="Jordan"
)

signup_result = repo.create_user(new_user)
print("Sign Up Result:", signup_result)

print("\n----------------------------------------\n")

# --- 3. Test Login ---
print("--- Testing Login ---")
login_result = repo.login_user("mohammad@example.com", "mySecretPassword123")
print("Login Result:", login_result)