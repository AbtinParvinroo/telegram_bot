# start_handler.py
from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    update.message.reply_text(f"سلام {user.first_name}, خوش آمدید به بات!")
