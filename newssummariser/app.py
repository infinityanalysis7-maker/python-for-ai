import streamlit as st
from get_news import get_news
from summarise import summarise
from dotenv import load_dotenv
import os

# Load keys
load_dotenv()
NEWS_API_KEY   = os.getenv("NEWS_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Page title
st.title("🗞️ AI News Summariser")
st.subheader("Latest India news summarised by AI")

# Button
if st.button("Get Latest News"):
    
    with st.spinner("Fetching news..."):
        articles = get_news(NEWS_API_KEY)
    
    for article in articles:
        title = article.get("title", "No title")
        description = article.get("description", "")
        content = article.get("content", "")
        full_text = f"{title}. {description}. {content}"
        
        with st.spinner(f"Summarising..."):
            summary = summarise(full_text, GEMINI_API_KEY)
        
        # Display as card
        st.markdown("---")
        st.markdown(f"### 📌 {title}")
        st.success(f"💡 {summary}")