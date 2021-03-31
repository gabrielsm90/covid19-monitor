"""
Logger service.

Keeps listening to the messages that arrive
in the Log topic and writes them to a configured
file.
"""

import os

from services.common.lib.config import Config
from services.common.lib.utils.covid_monitor_kafka import CovidMonitorKafkaConsumer


if __name__ == "__main__":
    log_listener = CovidMonitorKafkaConsumer(
        topic=Config.KAFKA_TOPIC_LOG, group_id="logger"
    )
    log_file_path = os.path.join(Config.LOG_DIR, Config.LOG_FILE)
    for message in log_listener.consume():
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{message}\n")
