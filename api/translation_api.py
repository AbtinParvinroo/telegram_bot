import requests

BASE_URL = "https://api.mymemory.translated.net/get"

def translate_text(text: str, source_lang: str = "auto", target_lang: str = "en") -> str:
    """
    ترجمه متن با استفاده از MyMemory API (رایگان)
    """
    params = {
        "q": text,
        "langpair": f"{source_lang}|{target_lang}"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        data = response.json()
        return data['responseData']['translatedText']
    except Exception as e:
        return f"خطا در ترجمه: {e}"
