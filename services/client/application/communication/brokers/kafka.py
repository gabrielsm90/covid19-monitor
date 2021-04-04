"""Module to provide communication with  Apache Kafka."""

import logging
from typing import Dict, Any

from common.lib.config import Config
from common.lib.communication.mom import Listener, Publisher
from common.lib.communication.mom.brokers.kafkamq import (
    CovidMonitorKafkaConsumer,
    CovidMonitorKafkaProducer,
)


logger = logging.getLogger(Config.LOG_NAME)


class KafkaNewJobListener(Listener):
    """Kafka listener for the scheduler topic."""

    def __init__(self, auto_offset_reset: str = "latest"):
        """Create new listener with data from configuration."""
        super().__init__(
            CovidMonitorKafkaConsumer(
                topic=Config.KAFKA["TOPIC_SCHEDULER"],
                group_id="api_client",
                auto_offset_reset=auto_offset_reset,
            )
        )

    def consume(self):
        """
        Consume new jobs.

        Method that keeps listening to the
        new jobs published.
        """
        for msg in self.listener.consume():
            yield msg


class KafkaCovidSummaryPublisher(Publisher):
    """Kafka publisher for summary topic."""

    def __init__(self):
        """Create new kafka producer with topic from configuration."""
        super().__init__(
            CovidMonitorKafkaProducer(topic=Config.KAFKA["TOPIC_COVID_SUMMARY"])
        )

    def publish(self, country_summary: Dict[str, Any]):
        """
        Publish covid summary to Kafka.

        Args:
            country_summary (Dict[str, Any]): Summary to
                be published.
        """
        logger.info(f"Publishing country stats: {country_summary}...")
        self.publisher.publish_message(country_summary)
