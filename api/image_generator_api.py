import requests

# جایگزین کن با کلید واقعی خودت
STABILITY_API_KEY = "your_stability_api_key"
BASE_URL = "https://api.stability.ai/v1/generation/stable-diffusion-v1-5/text-to-image"

def generate_image(prompt: str) -> bytes | None:
    """
    تولید تصویر از متن با استفاده از Stability AI
    """
    headers = {
        "Authorization": f"Bearer {STABILITY_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "text_prompts": [{"text": prompt}],
        "cfg_scale": 7,
        "height": 512,
        "width": 512,
        "samples": 1,
        "steps": 30,
    }

    try:
        response = requests.post(BASE_URL, headers=headers, json=payload)
        response.raise_for_status()
        image_bytes = response.content  # بسته به API ممکنه نیاز به decode باشه
        return image_bytes
    except Exception as e:
        print(f"[Image Generator] Error: {e}")
        return None
