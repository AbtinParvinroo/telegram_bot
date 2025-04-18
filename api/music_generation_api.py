import requests

# توجه: فرض بر اینه که از Suno یا یک سرویس مشابه استفاده می‌کنی که API داره.
# اگر Suno رسمی API نداره، این ساختار آماده‌ست برای آینده یا جایگزینی با سرویس مشابه

SUNO_API_KEY = "your_suno_api_key"
SUNO_BASE_URL = "https://api.suno.ai/generate"

def generate_music(prompt: str) -> str:
    """
    تولید لینک موسیقی از طریق متن ورودی
    """
    headers = {
        "Authorization": f"Bearer {SUNO_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": prompt,
        "style": "lofi"
    }

    try:
        response = requests.post(SUNO_BASE_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("music_url", "No music generated")
    except Exception as e:
        return f"[Music Generation Error] {e}"
