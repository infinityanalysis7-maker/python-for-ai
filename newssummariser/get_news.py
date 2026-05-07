import requests

def get_news(api_key):
    
    try:                              # try this whole block
        url = "https://newsapi.org/v2/everything"
        
        params = {
            "q": "india",
            "pageSize": 5,
            "language": "en",
            "sortBy": "publishedAt",
            "apiKey": api_key
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            return data["articles"]
        else:
            print(f"News API failed: {response.status_code}")
            return []
            
    except requests.ConnectionError:
        print("No internet connection!")  # specific error
        return []
        
    except Exception as e:
        print(f"Something went wrong: {e}")  # catches anything else
        return []