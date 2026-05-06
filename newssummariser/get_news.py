import requests

# This function fetches latest news
def get_news(api_key):
    
    # Changed to /everything — works on free plan
    url = "https://newsapi.org/v2/everything"
    
    # Parameters — filters we send to NewsAPI
    params = {
        "q": "india",        # search india news
        "pageSize": 5,       # only 5 articles
        "language": "en",    # english only
        "sortBy": "publishedAt",  # latest first
        "apiKey": api_key    # our secret key
    }
    
    # Make the request
    response = requests.get(url, params=params)
    
    # Check if it worked
    if response.status_code == 200:
        data = response.json()
        print(data)          # debug line — see what comes back
        return data["articles"]
    else:
        print("Failed:", response.status_code)
        return []