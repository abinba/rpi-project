import board
import busio
import adafruit_bme280.advanced as adafruit_bme280


class BME280Censor:
    """
    Class to initialize and read metrics from the censor
    """
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.bme = adafruit_bme280.Adafruit_BME280_I2C(i2c, 0x76)
        self.bme.sea_level_pressure = 1010
        self.bme.standby_period = adafruit_bme280.STANDBY_TC_500
        self.bme.iir_filter = adafruit_bme280.IIR_FILTER_X16

    def read(self):
        self.bme.overscan_pressure = adafruit_bme280.OVERSCAN_X16
        self.bme.overscan_humidity = adafruit_bme280.OVERSCAN_X1
        self.bme.overscan_temperature = adafruit_bme280.OVERSCAN_X2

        return {
            "temperature": self.bme.temperature,
            "humidity": self.bme.humidity,
            "pressure": self.bme.pressure
        }
