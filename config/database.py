import psycopg2
import os

class Database:
    # 🎯 الرابط السحابي الخاص بقاعدة بيانات Neon الخاصة بك
    DB_URL = "postgresql://neondb_owner:npg_IZD2qEWdFot6@ep-delicate-frog-ax9ah5k2-pooler.c-4.us-east-2.aws.neon.tech/neondb?sslmode=require"

    @classmethod
    def initialize(cls):
        try:
            conn = psycopg2.connect(cls.DB_URL)
            cursor = conn.cursor()
            
            # 🎯 إنشاء الجدول تلقائياً ببياناتك الجديدة أونلاين
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY, 
                    full_name VARCHAR(255) NOT NULL, 
                    email VARCHAR(255) UNIQUE NOT NULL, 
                    password VARCHAR(255) NOT NULL, 
                    phone VARCHAR(50) NOT NULL, 
                    gender VARCHAR(25) NOT NULL, 
                    date_of_birth DATE NOT NULL,
                    country VARCHAR(50) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            conn.commit()
            cursor.close()
            conn.close()
            print("Connected to Neon Cloud Database & Table Verified Successfully!")
            return True
        except Exception as e:
            print(f"Cloud Database connection error: {e}")
            return False

    @classmethod
    def get_connection(cls):
        return psycopg2.connect(cls.DB_URL)