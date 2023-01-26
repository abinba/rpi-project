import time

from influxdb import InfluxDBClient

from core.config import INFLUXDB_HOST, INFLUXDB_PORT, INFLUXDB_USER, INFLUXDB_PASSWORD, INFLUXDB_DB


class InfluxDB:
    def __init__(self):
        self.influx_client = InfluxDBClient(
            host=INFLUXDB_HOST,
            port=INFLUXDB_PORT,
            username=INFLUXDB_USER,
            password=INFLUXDB_PASSWORD,
            database=INFLUXDB_DB,
        )

    def send(self, parameters):
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
