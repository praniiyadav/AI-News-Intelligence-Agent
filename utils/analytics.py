import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def show_sentiment_chart(sentiment_list):

    sentiment_df = pd.DataFrame(sentiment_list, columns=["Sentiment"])

    sentiment_count = sentiment_df["Sentiment"].value_counts()

    plt.style.use("dark_background")

    fig, ax = plt.subplots(figsize=(5, 5), facecolor="#0f172a")

    ax.set_facecolor("#0f172a")

    colors = []

    for sentiment in sentiment_count.index:

        if sentiment == "Positive":
            colors.append("#22c55e")

        elif sentiment == "Negative":
            colors.append("#ef4444")

        else:
            colors.append("#f59e0b")

    ax.pie(
        sentiment_count.values,
        labels=sentiment_count.index,
        autopct="%1.1f%%",
        colors=colors,
        startangle=90,
    )

    ax.set_title("Sentiment Analysis")

    st.pyplot(fig)


def show_category_chart(category_list):

    category_df = pd.DataFrame(category_list, columns=["Category"])

    category_count = category_df["Category"].value_counts()

    fig, ax = plt.subplots(figsize=(5, 5), facecolor="#0f172a")

    ax.set_facecolor("#0f172a")

    bars = ax.bar(category_count.index, category_count.values)

    for bar in bars:

        height = bar.get_height()

        ax.text(
            bar.get_x() + bar.get_width() / 2, height, str(int(height)), ha="center"
        )

    ax.set_title("News Categories")

    st.pyplot(fig)
