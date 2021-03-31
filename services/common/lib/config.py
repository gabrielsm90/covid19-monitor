"""Configuration module."""

from os import getenv


class Config:
    """Configuration data to be used throughout the services."""

    # Covid 19 API's URL, from where the stats are fetched.
    COVID_API_URL = getenv("COVID_API_URL", "https://api.covid19api.com/summary")

    # Kafka's host.
    KAFKA_BOOTSTRAP_SERVER = getenv("KAFKA_BOOTSTRAP_SERVER", "localhost:9093")

    # Kafka's topic populated with the data returned from the API.
    KAFKA_TOPIC_COVID_SUMMARY = getenv(
        "KAFKA_TOPIC_COVID_SUMMARY", "COVID_MONITOR_SUMMARY"
    )

    # Kafka's topic populated with log messages.
    KAFKA_TOPIC_LOG = getenv("KAFKA_TOPIC_LOG", "COVID_MONITOR_LOG")

    # Kafka's topic populated with new jobs. That triggers the fetching process.
    KAFKA_TOPIC_SCHEDULER = getenv("KAFKA_TOPIC_SCHEDULER", "COVID_MONITOR_SCHEDULER")

    # Log's directory.
    LOG_DIR = getenv("LOG_DIR", r"C:\tmp\covid19-monitor")

    # Log file's name.
    LOG_FILE = getenv("LOG_FILE", "covid19-monitor.log")

    LOG_NAME = getenv("LOG_NAME", "covid19")

    # Mongodb's host.
    MONGO_HOST = getenv("MONGO_HOST", "localhost")

    # Interval to be followed by the scheduler (in minutes)
    NEW_JOB_INTERVAL = int(getenv("NEW_JOB_INTERVAL", 1))

    # URL where the web app will be served.
    SERVER_URL = getenv("SERVER_URL", "http://0.0.0.0:5000")
