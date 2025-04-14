import re

def extract_birth_info(message):
    match = re.findall(r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}', message)
    return match[0] if match else "Not provided"

def detect_query_type(msg):
    msg = msg.lower()
    if "horoscope" in msg or "zodiac" in msg:
        return "astrology"
    elif "number" in msg or "numerology" in msg:
        return "numerology"
    elif "palm" in msg or "hand" in msg:
        return "palmistry"
    return "general spiritual guidance"
