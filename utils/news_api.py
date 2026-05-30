import requests
import os

NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def fetch_news(topic):

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={topic}&"
        f"language=en&"
        f"pageSize=5&"
        f"sortBy=publishedAt&"
        f"apiKey={NEWS_API_KEY}"
    )

    response = requests.get(url)

    data = response.json()

    return data.get("articles", [])
