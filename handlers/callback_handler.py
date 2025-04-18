# callback_handler.py
from telegram import Update
from telegram.ext import CallbackContext

def handle_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"دکمه {query.data} انتخاب شد!")
