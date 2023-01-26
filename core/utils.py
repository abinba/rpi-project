import requests

from core.config import BOT_TOKEN, CHAT_ID


def send_message(message: str):
    return requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/"
        f"sendMessage?text={message}&chat_id={CHAT_ID}"
    )
