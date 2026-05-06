import requests

def summarise(text, api_key):

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
    else:
        print("Gemini error:", response.status_code, response.text)
        return "Could not summarise"