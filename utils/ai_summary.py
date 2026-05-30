from groq import Groq
import os


def generate_summary(news_text):

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    prompt = f"""
Summarize these latest news articles
into short professional bullet points.

News:
{news_text}
"""

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant", messages=[{"role": "user", "content": prompt}]
    )

    return completion.choices[0].message.content
