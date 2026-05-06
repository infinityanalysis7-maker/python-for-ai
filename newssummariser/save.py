# This function saves our summaries to a file
def save_results(articles):

    # Open a file to write into
    with open("news_summary.txt", "w", encoding="utf-8") as file:
        
        file.write("=== TODAY'S NEWS SUMMARY ===\n\n")
        
        # Loop through each article and write it
        for i, article in enumerate(articles):
            file.write(f"Article {i+1}\n")
            file.write(f"Title: {article['title']}\n")
            file.write(f"Summary: {article['summary']}\n")
            file.write("-" * 40 + "\n\n")
    
    print("✅ Saved to news_summary.txt")