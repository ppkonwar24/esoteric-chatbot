from openai import OpenAI
import os
from dotenv import load_dotenv
from utils import extract_birth_info, detect_query_type

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def handle_message(user_id, user_message):
    query_type = detect_query_type(user_message)
    birth_info = extract_birth_info(user_message)

    system_prompt = f"You are an expert in {query_type}. Provide helpful esoteric guidance."
    full_prompt = f"{system_prompt}\n\nUser's message: {user_message}\nBirth info: {birth_info}"

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": full_prompt}
        ]
    )

    return response.choices[0].message.content
