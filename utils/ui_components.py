import streamlit as st


def news_card(title, sentiment, category, description):

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
