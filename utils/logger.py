import logging

# تعریف تنظیمات لاگ
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("MyTelegramBot")
