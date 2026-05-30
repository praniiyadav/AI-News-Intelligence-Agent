from groq import Groq
import os


def generate_chat_response(user_question):

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": user_question}],
    )

    return completion.choices[0].message.content
