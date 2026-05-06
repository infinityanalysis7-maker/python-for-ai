# Import our own files
from get_news import get_news
from summarise import summarise
from save import save_results

# Your API keys — paste your actual keys here
NEWS_API_KEY   = "912af9536e924944837cff0436de15b8"
GEMINI_API_KEY = "AIzaSyA4Cn0Bngh2jpHz0p83e-wbCuG2iaTuYp4"

# Main function — connects everything
def main():
    
    print("📰 Fetching latest news...")
    articles = get_news(NEWS_API_KEY)
    
    print("🤖 Summarising with AI...")
    results = []
    
    for article in articles:
        # Get title and description
        title = article.get("title", "No title")
        description = article.get("description", "")
        content = article.get("content", "")
        
        # Combine description and content for better summary
        full_text = f"{title}. {description}. {content}"
        
        # Get AI summary
        summary = summarise(full_text, GEMINI_API_KEY)
        
        # Store result
        results.append({
            "title": title,
            "summary": summary
        })
        
        # Print to screen
        print(f"\n📌 {title}")
        print(f"💡 {summary}")
        print("-" * 40)
    
    # Save everything
    save_results(results)

# Run it
main()