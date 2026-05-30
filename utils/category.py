import re


def classify_news(text):

    # ==============================
    # CLEAN TEXT
    # ==============================
    text = str(text).lower()

    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    # ==============================
    # TECHNOLOGY
    # ==============================
    technology_keywords = [
        "ai",
        "openai",
        "chatgpt",
        "machine learning",
        "artificial intelligence",
        "robot",
        "automation",
        "technology",
        "google",
        "microsoft",
        "apple",
        "software",
        "gemini",
        "groq",
        "llm",
        "deep learning",
    ]

    # ==============================
    # POLITICS
    # ==============================
    politics_keywords = [
        "government",
        "minister",
        "election",
        "politics",
        "cm",
        "prime minister",
        "parliament",
        "tdp",
        "bjp",
        "congress",
        "president",
        "mla",
        "mp",
        "assembly",
        "cabinet",
    ]

    # ==============================
    # BUSINESS
    # ==============================
    business_keywords = [
        "stock",
        "market",
        "business",
        "startup",
        "finance",
        "economy",
        "investment",
        "share",
        "company",
        "revenue",
        "profit",
        "bank",
        "trading",
    ]

    # ==============================
    # SPORTS
    # ==============================
    sports_keywords = [
        "cricket",
        "football",
        "ipl",
        "sports",
        "captain",
        "match",
        "stadium",
        "team",
        "player",
        "kohli",
        "dhoni",
        "virat",
        "world cup",
        "tournament",
    ]

    # ==============================
    # ENTERTAINMENT
    # ==============================
    entertainment_keywords = [
        "movie",
        "actor",
        "cinema",
        "music",
        "film",
        "director",
        "netflix",
        "ott",
        "song",
        "trailer",
        "celebrity",
        "hero",
        "actress",
    ]

    # ==============================
    # CATEGORY CHECK
    # ==============================

    for keyword in technology_keywords:

        if keyword in text:
            return "Technology"

    for keyword in politics_keywords:

        if keyword in text:
            return "Politics"

    for keyword in business_keywords:

        if keyword in text:
            return "Business"

    for keyword in sports_keywords:

        if keyword in text:
            return "Sports"

    for keyword in entertainment_keywords:

        if keyword in text:
            return "Entertainment"

    # ==============================
    # DEFAULT
    # ==============================
    return "General"
