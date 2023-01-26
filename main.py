from time import sleep

import requests

from luma.oled.device import ssd1331

from core.ai import AI
from core.censors import BME280Censor
from core.config import BOT_TOKEN
from core.grafana import Grafana


def send_message_to_telegram_bot(message):
    return requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/"
        f"sendMessage?text={message}&chat_id=48355225"
    )


if __name__ == "__main__":
    disp = ssd1331()
    disp.clear()

    bme = BME280Censor()
    grafana = Grafana()

    while True:
        parameters = bme.read()
        grafana.send_data_to_influxdb(parameters=parameters)

        ai = AI(
            temperature=parameters["temperature"],
            pressure=parameters["pressure"],
            humidity=parameters["humidity"]
        )

        response = ai.get_conditions_status(prompt=ai.generate_prompt())

        send_message_to_telegram_bot(message=response)
        sleep(5)
