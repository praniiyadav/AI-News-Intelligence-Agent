import streamlit as st
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

from utils.sentiment import analyze_sentiment
from utils.category import classify_news
from utils.news_api import fetch_news
from utils.ai_summary import generate_summary
from utils.email_service import send_email
from utils.analytics import (
    show_sentiment_chart,
    show_category_chart,
)
from utils.chatbot import generate_chat_response

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "chat_answer" not in st.session_state:
    st.session_state.chat_answer = ""


# ==========================================
# LOAD CSS
# ==========================================
def load_css():

    with open("assets/styles.css", encoding="utf-8") as f:

        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css()


# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="AI News Intelligence Agent",
    page_icon="icon-192.png",
    layout="wide",
)


# ==========================================
# HERO SECTION
# ==========================================
st.markdown(
    """
<div class="hero-title">
🚀 AI News Intelligence Agent
</div>

<div class="hero-subtitle">
Real-time AI-powered news analytics,
sentiment tracking,
summarization &
email automation dashboard
</div>
""",
    unsafe_allow_html=True,
)


# ==========================================
# INFO
# ==========================================
st.info(
    "📩 Enter any topic and receive AI summarized latest news directly to your email."
)


# ==========================================
# INPUTS
# ==========================================
col1, col2 = st.columns(2)

with col1:

    topic = st.text_input("📰 Enter Topic", placeholder="Artificial Intelligence")

with col2:

    receiver_email = st.text_input("📧 Receiver Email", placeholder="example@gmail.com")


# ==========================================
# BUTTON
# ==========================================
if st.button("Send News Email 🚀"):

    if not topic:

        st.warning("⚠ Please enter a topic")

    elif not receiver_email:

        st.warning("⚠ Please enter receiver email")

    else:

        try:

            with st.spinner("🤖 Fetching latest news..."):

                articles = fetch_news(topic)

                if len(articles) == 0:

                    st.error("❌ No news found")

                else:

                    sentiment_list = []
                    category_list = []

                    st.markdown(
                        """
<div class="section-title">
📰 Latest News Articles
</div>
""",
                        unsafe_allow_html=True,
                    )

                    news_text = ""

                    for article in articles:

                        title = article.get("title", "No Title")

                        description = article.get("description", "")

                        if not description:

                            continue

                        sentiment = analyze_sentiment(description)

                        category = classify_news(description)

                        sentiment_list.append(sentiment)

                        category_list.append(category)

                        st.markdown(
                            f"""
<div class="news-card">

<div class="news-title">
{title}
</div>

<div class="sentiment-tag">
📊 {sentiment}
</div>

<div class="category-tag">
🏷 {category}
</div>

<div class="news-description">
{description}
</div>

</div>
""",
                            unsafe_allow_html=True,
                        )

                        news_text += f"{title}\n" f"{description}\n\n"

                    # ==================================
                    # AI SUMMARY
                    # ==================================
                    summary = generate_summary(news_text)
                    st.session_state.summary = summary

                    # ==================================
                    # EMAIL
                    # ==================================
                    send_email(receiver_email, topic, summary)

                    st.success("✅ Email sent successfully!")

                    # ==================================
                    # ANALYTICS
                    # ==================================
                    st.markdown(
                        """
<div class="analytics-card">

<div class="section-title">
📊 News Analytics Dashboard
</div>

</div>
""",
                        unsafe_allow_html=True,
                    )

                    col1, col2 = st.columns(2)

                    with col1:

                        show_sentiment_chart(sentiment_list)

                    with col2:

                        show_category_chart(category_list)

                    # ==================================
                    # SUMMARY
                    # ==================================
                    st.markdown(
                        f"""
<div class="summary-card">

<div class="section-title">
🧠 AI Generated Summary
</div>

<div class="news-description">
{summary}
</div>

</div>
""",
                        unsafe_allow_html=True,
                    )

        except Exception as e:

            st.error(f"❌ Error: {e}")
# ==================================
# AI NEWS CHATBOT
# ==================================

if st.session_state.summary:

    st.markdown(
        """
<div class="section-title">
🤖 AI News Chatbot
</div>
""",
        unsafe_allow_html=True,
    )

    question = st.text_input("Ask anything about the latest news", key="chat_question")

    if st.button("Ask AI"):

        try:

            answer = generate_chat_response(f"""
You are an AI News Assistant.

News Summary:

{st.session_state.summary}

User Question:

{question}

Answer only based on the news summary.
""")

            st.session_state.chat_answer = answer

        except Exception as e:

            st.error(f"Chatbot Error: {e}")

    if st.session_state.chat_answer:

        st.markdown(
            f"""
<div class="summary-card">

<div class="news-description">
{st.session_state.chat_answer}
</div>

</div>
""",
            unsafe_allow_html=True,
        )
