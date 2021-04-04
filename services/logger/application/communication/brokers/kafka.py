"""Module the provides a Kafka Consumer."""

from common.lib.config import Config
from common.lib.communication.mom import Listener
from common.lib.communication.mom.brokers.kafkamq import CovidMonitorKafkaConsumer


class KafkaCovidLogListener(Listener):
    """Kafka listener for the log topic."""

    def __init__(self, auto_offset_reset="latest"):
        """Create new listener with data from configuration."""
        super().__init__(
            CovidMonitorKafkaConsumer(
                topic=Config.KAFKA["TOPIC_LOG"],
                group_id="logger",
                auto_offset_reset=auto_offset_reset,
            )
        )

    def consume(self):
        """Consume Log topic."""
        for msg in self.listener.consume():
            yield msg
