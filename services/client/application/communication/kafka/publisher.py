"""Module the provides a Kafka Publisher."""

import logging
from typing import Any, Dict

from common.lib.config import Config
from common.lib.utils.covid_monitor_kafka import CovidMonitorKafkaProducer


logger = logging.getLogger(Config.LOG_NAME)


class CovidSummaryPublisher(CovidMonitorKafkaProducer):
    """Kafka publisher for summary topic."""

    def __init__(self):
        """Create new producer with topic from configuration."""
        super().__init__(topic=Config.KAFKA_TOPIC_COVID_SUMMARY)

    def publish_summary(self, country_summary: Dict[str, Any]):
        """
        Publish covid summary to Kafka.

        Args:
            country_summary (Dict[str, Any]): Summary to
                be published.
        """
        logger.info(f"Publishing country stats: {country_summary}...")
        self.publish_message(country_summary)
