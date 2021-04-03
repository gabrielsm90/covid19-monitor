"""Module the provides a Kafka Consumer."""

from common.lib.config import Config
from common.lib.utils.covid_monitor_kafka import CovidMonitorKafkaConsumer


class CovidLogListener(CovidMonitorKafkaConsumer):
    """Kafka listener for the log topic."""

    def __init__(self):
        """Create new listener with data from configuration."""
        super().__init__(topic=Config.KAFKA_TOPIC_LOG, group_id="logger")
