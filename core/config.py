import os

SEA_LEVEL = 1010

OPENAI_API_KEY = os.environ.get("OPEN_AI_KEY")
OPENAI_MAX_TOKENS = os.environ.get("OPENAI_MAX_TOKENS", 500)
OPENAI_ENGINE = "text-davinci-002"

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

INFLUXDB_HOST = os.environ.get("INFLUXDB_HOST", "localhost")
INFLUXDB_PORT = os.environ.get("INFLUXDB_PORT", 8086)
INFLUXDB_USER = os.environ.get("INFLUXDB_USER", "admin")
INFLUXDB_PASSWORD = os.environ.get("INFLUXDB_PASSWORD", "admin")
INFLUXDB_DB = os.environ.get("INFLUXDB_DB", "censors")
