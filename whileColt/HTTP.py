import requests

url1 = 'https://theskullery.net/'
url2 = "https://icanhazdadjoke.com/"

response = requests.get(url2, headers={"Accept": "application/json"})
data = response.json()

print(f"your request to {url2} came back with status code {response.status_code}")
print(data['joke'])
