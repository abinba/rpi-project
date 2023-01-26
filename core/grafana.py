import time

from influxdb import InfluxDBClient


class Grafana:
    def __init__(self):
        self.influx_client = InfluxDBClient(
            host="localhost",
            port=8086,
            username="admin",
            password="admin",
            database="censors",
        )

    def send_data_to_influxdb(self, parameters):
        iso = time.ctime()
        self.influx_client.write_points([
            {
                "measurement": "temperature",
                "tags": {
                    "sensor_id": "BME280"
                },
                "time": iso,
                "fields": {
                    "value": parameters["temperature"],
                }
            },
            {
                "measurement": "humidity",
                "tags": {
                    "sensor_id": "BME280"
                },
                "time": iso,
                "fields": {
                    "value": parameters["humidity"],
                }
            },
            {
                "measurement": "pressure",
                "tags": {
                    "sensor_id": "BME280"
                },
                "time": iso,
                "fields": {
                    "value": parameters["pressure"],
                }
            },
        ])
