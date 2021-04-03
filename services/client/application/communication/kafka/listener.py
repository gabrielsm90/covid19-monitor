"""Module the provides a Kafka Consumer."""

from common.lib.config import Config
from common.lib.utils.covid_monitor_kafka import CovidMonitorKafkaConsumer


class CovidNewJobListener(CovidMonitorKafkaConsumer):
    """Kafka listener for the scheduler topic."""

    def __init__(self):
        """Create new listener with data from configuration."""
        super().__init__(topic=Config.KAFKA_TOPIC_SCHEDULER, group_id="api_client")
