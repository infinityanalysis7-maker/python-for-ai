import requests

api_key = "AIzaSyA4Cn0Bngh2jpHz0p83e-wbCuG2iaTuYp4"

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"

response = requests.get(url)
data = response.json()

for model in data["models"]:
    print(model["name"])