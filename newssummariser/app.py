import streamlit as st
from get_news import get_news
from summarise import summarise
from database import save_article, get_saved_articles
from dotenv import load_dotenv
import os

load_dotenv()
NEWS_API_KEY   = os.getenv("NEWS_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

st.title("🗞️ AI News Summariser")
st.subheader("Latest India news summarised by AI")

# Two tabs
tab1, tab2 = st.tabs(["📰 Latest News", "🔖 Saved Articles"])

with tab1:
    if st.button("Get Latest News"):
        
        with st.spinner("Fetching news..."):
            articles = get_news(NEWS_API_KEY)
        
        for article in articles:
            title       = article.get("title", "No title")
            description = article.get("description", "")
            content     = article.get("content", "")
            full_text   = f"{title}. {description}. {content}"
            
            with st.spinner(f"Summarising..."):
                summary = summarise(full_text, GEMINI_API_KEY)
            
            st.markdown("---")
            st.markdown(f"### 📌 {title}")
            st.success(f"💡 {summary}")
            
            # Save button for each article
            if st.button(f"🔖 Save", key=title):
                if save_article(title, summary):
                    st.success("✅ Saved!")
                else:
                    st.error("❌ Could not save")

with tab2:
    st.subheader("Your Saved Articles")
    
    saved = get_saved_articles()
    
    if not saved:
        st.info("No saved articles yet — save some from Latest News!")
    else:
        for article in saved:
            st.markdown("---")
            st.markdown(f"### 📌 {article['title']}")
            st.success(f"💡 {article['summary']}")
            st.caption(f"Saved at: {article['saved_at']}")