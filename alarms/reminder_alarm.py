import asyncio
from datetime import datetime, timedelta
from services.database_service import get_due_reminders, mark_reminder_sent
from telegram import Bot
from config.config import TELEGRAM_BOT_TOKEN

bot = Bot(token=TELEGRAM_BOT_TOKEN)

async def reminder_loop():
    """
    حلقه‌ی اصلی بررسی یادآوری‌ها
    هر 30 ثانیه یادآوری‌هایی که موعدشان رسیده را بررسی می‌کند.
    """
    while True:
        try:
            now = datetime.utcnow()
            due_reminders = await get_due_reminders(now)

            for reminder in due_reminders:
                await send_reminder(reminder)
                await mark_reminder_sent(reminder["id"])

        except Exception as e:
            print(f"[Reminder Alarm] Error: {e}")

        await asyncio.sleep(30)  # بررسی در هر 30 ثانیه

async def send_reminder(reminder: dict):
    """
    ارسال پیام یادآوری به کاربر
    """
    user_id = reminder["user_id"]
    text = reminder["text"]
    repeat = reminder.get("repeat")  # daily, weekly, etc.

    message = f"⏰ یادآوری: {text}"
    try:
        await bot.send_message(chat_id=user_id, text=message)
    except Exception as e:
        print(f"[Reminder Alarm] Failed to send message: {e}")
