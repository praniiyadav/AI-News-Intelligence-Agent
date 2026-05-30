# 🚀 AI News Intelligence Agent

An end-to-end AI-powered News Intelligence and Analytics Platform built using Python, Streamlit, Groq LLM, and NewsAPI.

The application enables users to fetch real-time news articles on any topic, perform sentiment analysis, classify news categories, generate AI-powered summaries, visualize analytics, interact with a news-focused AI chatbot, and automatically deliver summarized news through email.

---

# 📌 Features

* 📰 Real-time News Fetching using NewsAPI
* 🤖 AI-Powered News Summarization using Groq LLM (Llama 3.1 8B Instant)
* 😊 Sentiment Analysis (Positive, Negative, Neutral)
* 🏷️ Intelligent News Category Classification
* 📊 Interactive Analytics Dashboard
* 💬 AI News Chatbot for News-Based Q&A
* 📧 Automated Email Delivery using SMTP
* 🔍 Topic-Based News Search
* 🎨 Modern and Responsive Streamlit UI
* 🔐 Secure API Key Management using `.env`
* ⚡ Real-Time News Processing Workflow

---

# 🛠 Tech Stack

## Frontend

* Streamlit

## Backend

* Python

## APIs & AI Models

* NewsAPI
* Groq API
* Llama 3.1 8B Instant

## Data Analysis & Visualization

* Pandas
* Matplotlib

## Python Libraries

* streamlit
* requests
* groq
* python-dotenv
* pandas
* matplotlib
* textblob

---

# 📂 Project Structure

AI-News-Intelligence-Agent/

├── app.py

├── .env

├── requirements.txt

├── assets/

│ └── styles.css

├── utils/

│ ├── news_api.py

│ ├── sentiment.py

│ ├── category.py

│ ├── ai_summary.py

│ ├── chatbot.py

│ ├── analytics.py

│ ├── email_service.py

│ └── ui_components.py

├── screenshots/

└── README.md

---

# ⚙️ Installation & Setup

## Clone Repository

```bash
git clone https://github.com/praniiyadav/AI-News-Intelligence-Agent.git
```

## Move to Project Directory

```bash
cd AI-News-Intelligence-Agent
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Create .env File

```env
GROQ_API_KEY=your_groq_api_key

NEWS_API_KEY=your_newsapi_key

EMAIL_ADDRESS=your_email@gmail.com

EMAIL_PASSWORD=your_gmail_app_password
```

## Run Application

```bash
streamlit run app.py
```

---

# 🔄 Application Workflow

User Enters Topic & Email

↓

NewsAPI Fetches Latest Articles

↓

Sentiment Analysis

↓

News Category Classification

↓

AI Summary Generation (Groq LLM)

↓

Analytics Dashboard Generation

↓

Email Automation (SMTP)

↓

AI News Chatbot Interaction

↓

Results Displayed to User

---

# 📊 Dashboard Analytics

The application provides:

* Sentiment Distribution Pie Chart
* News Category Analytics Bar Chart
* AI Generated Summary Panel
* Interactive News Cards
* News-Based AI Chatbot
* Real-Time Analytics Visualization

---

# 💬 AI News Chatbot

The integrated AI chatbot allows users to interact with the generated news summary and ask contextual questions such as:

* What are today's key highlights?
* Summarize the politics news.
* Which news has positive sentiment?
* Explain the technology news.
* What happened in Andhra politics?

This enables a more interactive and intelligent news exploration experience.

---

# 🧠 Key Learning Outcomes

This project helped in understanding:

* REST API Integration
* Large Language Model (LLM) Workflows
* Prompt Engineering
* Streamlit Application Development
* AI-Powered Summarization
* Sentiment Analysis
* Text Classification
* Real-Time Data Processing
* Email Automation
* Analytics Dashboard Development
* Environment Variable Security
* Modular Project Architecture

---

# 🚀 Future Improvements

* Personalized News Recommendations
* Multi-Language Summarization
* Daily Scheduled News Delivery
* Voice-Based News Assistant
* RAG-Based News Search
* User Authentication System
* Database Integration
* Advanced NLP Pipelines
* News Recommendation Engine
* AI-Powered Trend Analysis

---

# 📌 Project Status

## ✅ Completed

* Real-Time News Fetching
* AI News Summarization
* Sentiment Analysis
* News Category Classification
* Analytics Dashboard
* AI News Chatbot
* Email Automation
* Interactive Visualizations
* Professional UI Design

## 🔄 Planned

* Personalized Recommendations
* RAG Integration
* Voice Assistant
* Advanced AI Workflows

---

# 👨‍💻 Author

### Praneeth Mopuri

GitHub:
https://github.com/praniiyadav

LinkedIn:
https://www.linkedin.com/in/praniiyadav/

---

⭐ If you found this project useful, consider giving it a star on GitHub.

