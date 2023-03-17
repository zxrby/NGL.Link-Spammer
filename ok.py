import requests

url = "https://ngl.link/api/submit"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://ngl.link",
    "Referer": "https://ngl.link/z7hejan"
}

data = {
    "username": "TARGET HERE",
    "question": "UR QUESTION HERE",
    "deviceId": "cfd278d9-b21d-444d-8a6f-6e7494f84bf8",
    "gameSlug": "",
    "referrer": ""
}

# amount of the spamms
num_requests = 100 

for i in range(num_requests):
    response = requests.post(url, headers=headers, data=data)
    print(f"Request {i+1}: {response.status_code}")
