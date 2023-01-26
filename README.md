# Raspberry PI Study Project

## Overview

This study project (Introduction to IoT) reads sensor data from a Raspberry Pi (RPi) 
and sends it to an InfluxDB database. The data is then displayed on a Grafana dashboard and 
analyzed by a ChatGPT AI to provide a status on the current 
conditions and potentially give advice on what actions to take.

## Setup
- Install the necessary libraries by running `pip install -r requirements.txt`.
- In order to run InfluxDB and Grafana use `docker-compose up -d`.
- Run the script `main.py` to start collecting sensor data and sending it to the InfluxDB.

## Dependencies
- Python 3
- InfluxDB 1.6
- Grafana
- ChatGPT AI
- BME280 sensor for temperature, pressure, and humidity readings

## Usage

The script `main.py` is the main entry point of the program. 
It initializes the BME280 sensor, InfluxDB, and ChatGPT AI, and then enters a 
loop to read sensor data, send it to InfluxDB, and use ChatGPT to analyze the 
data and provide a status on the current conditions. The script also sends the 
conditions status to the user via the `send_message` function to Telegram. The loop is set to 
run every 5 seconds but can be adjusted as needed.
