import os

# API Token برای چت‌بات
API_TOKEN = os.getenv("API_TOKEN", "your-telegram-bot-token")

# تنظیمات Redis
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)

# تنظیمات پایگاه‌داده PostgreSQL
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", 5432)
DB_NAME = os.getenv("DB_NAME", "telegram_bot_db")
DB_USER = os.getenv("DB_USER", "your_db_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "your_db_password")
