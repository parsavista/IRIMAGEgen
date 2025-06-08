import requests

bot_token = '7637390285:AAHv_nWEZcvbZ9yTnQCklcpkTn8X-dFiN5o'  # توکن بات شما

url = f"https://api.telegram.org/bot{bot_token}/deleteWebhook"

response = requests.post(url)
print(response.json())

