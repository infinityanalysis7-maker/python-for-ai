import requests

def summarise(text, api_key):
    
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

        body = {
            "contents": [{
                "parts": [{
                    "text": f"Summarise this news in 2-3 simple lines:\n\n{text}"
                }]
            }]
        }

        response = requests.post(url, json=body)

        if response.status_code == 200:
            data = response.json()
            summary = data["candidates"][0]["content"]["parts"][0]["text"]
            return summary
        
        elif response.status_code == 503:
            return "Gemini is busy right now — try again in a moment"
        
        else:
            return f"Could not summarise — error {response.status_code}"

    except requests.ConnectionError:
        return "No internet connection!"
    
    except Exception as e:
        return f"Something went wrong: {e}"