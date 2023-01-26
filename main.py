from time import sleep

from core.ai import AI
from core.censors import BME280Censor
from core.influxdb_ import InfluxDB
from core.utils import send_message


if __name__ == "__main__":
    # Initialize censor for temperature, pressure and humidity
    bme = BME280Censor()

    # Initialize grafana
    influx_db = InfluxDB()

    # Initialize ChatGPT AI
    ai = AI()

    while True:
        # Read parameters from the censor
        parameters = bme.read()

        # Send parameters to influxdb, whenever the parameters are sent to
        # influxdb, they should appear in Grafana dashboard
        influx_db.send(parameters=parameters)

        # Get conditions status
        response = ai.get_conditions_status(
            prompt=ai.generate_prompt(
                parameters=parameters
            )
        )

        # Send conditions status to user
        send_message(message=response)
        sleep(5)
