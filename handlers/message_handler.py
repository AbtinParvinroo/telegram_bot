# message_handler.py
from telegram import Update
from telegram.ext import CallbackContext

def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    update.message.reply_text(f"شما نوشته‌اید: {text}")
