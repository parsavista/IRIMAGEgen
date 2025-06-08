import requests

token = "7637390285:AAHv_nWEZcvbZ9yTnQCklcpkTn8X-dFiN5o"
url = f"https://api.telegram.org/bot{token}/deleteWebhook"
response = requests.post(url)
print(response.json())

