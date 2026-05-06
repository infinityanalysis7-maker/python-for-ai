from get_news import get_news
from summarise import summarise
from save import save_results
from dotenv import load_dotenv
import os

# Load keys from .env file
load_dotenv()

# Keys come from .env now
NEWS_API_KEY   = os.getenv("NEWS_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Main function — connects everything
def main():
    
    print("📰 Fetching latest news...")
    articles = get_news(NEWS_API_KEY)
    
    print("🤖 Summarising with AI...")
    results = []
    
    for article in articles:
        title = article.get("title", "No title")
        description = article.get("description", "")
        content = article.get("content", "")
        
        full_text = f"{title}. {description}. {content}"
        
        summary = summarise(full_text, GEMINI_API_KEY)
        
        results.append({
            "title": title,
            "summary": summary
        })
        
        print(f"\n📌 {title}")
        print(f"💡 {summary}")
        print("-" * 40)
    
    save_results(results)

main()