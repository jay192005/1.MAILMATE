from openai import OpenAI
import streamlit as st

# Correct usage for v1.x SDK
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_email_response(email_text, tone):
    prompt = f"""
You are an AI assistant. Write a reply to the following email using a {tone.lower()} tone:

Email:
{email_text}

Reply:
"""
    response = client.chat.completions.create(
        model="gpt-4o",  # or gpt-3.5-turbo
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
