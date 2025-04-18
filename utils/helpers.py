from datetime import datetime, timedelta

def time_converter(time_str: str) -> datetime:
    """
    ورودی: رشته‌ای مثل '5m', '2h', '1d'
    خروجی: زمان آینده بر اساس اکنون
    """
    unit = time_str[-1]
    value = int(time_str[:-1])
    now = datetime.now()

    if unit == 'm':
        return now + timedelta(minutes=value)
    elif unit == 'h':
        return now + timedelta(hours=value)
    elif unit == 'd':
        return now + timedelta(days=value)
    else:
        raise ValueError("فرمت زمان نامعتبر است. فقط از m، h، d استفاده کن.")

def format_datetime(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M")

def is_valid_time_format(time_str: str) -> bool:
    return time_str.endswith(('m', 'h', 'd')) and time_str[:-1].isdigit()
