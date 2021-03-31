"""

Logging module.

Defines a Kafka Logging Handler and sets up the
application's logger.

"""

import logging

from services.common.lib.utils.covid_monitor_kafka import CovidMonitorKafkaProducer
from services.common.lib.config import Config


class KafkaLoggingHandler(logging.StreamHandler):
    """
    Kafka Logging Handler.

    Logs all messages to a dedicated topic in the
    Message Queue.
    """

    def __init__(self):
        """
        Create new Kafka Logging Handler.

        Defines only one specific attribute called
        producer that will publish the log messages
        to the Message broker.
        """
        super(KafkaLoggingHandler, self).__init__()
        self.producer = CovidMonitorKafkaProducer(Config.KAFKA_TOPIC_LOG)

    def emit(self, record):
        """
        Publish log record to message broker.

        Args:
            record: Log message.
        """
        self.producer.publish_message({"message": self.format(record)})


# Setup application's logger.
logger = logging.getLogger(Config.LOG_NAME)
logger.setLevel(logging.INFO)
logger.addHandler(KafkaLoggingHandler())
