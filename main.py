import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from handlers import start_handler, callback_handler, message_handler

# فعال کردن لاگ‌ها
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # ساخت آپدیتر و دیسپچر
    updater = Updater("your-telegram-bot-token", use_context=True)
    dp = updater.dispatcher

    # اضافه کردن هندلرها
    dp.add_handler(CommandHandler("start", start_handler.start))
    dp.add_handler(CallbackQueryHandler(callback_handler.handle_callback))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler.handle_message))

    # شروع بات
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
