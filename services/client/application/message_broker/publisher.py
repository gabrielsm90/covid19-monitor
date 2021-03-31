import logging

from services.common.lib.config import Config
from services.common.lib.utils.covid_monitor_kafka import CovidMonitorKafkaProducer


logger = logging.getLogger(Config.LOG_NAME)


class CovidSummaryPublisher(CovidMonitorKafkaProducer):
    def __init__(self):
        super().__init__(topic=Config.KAFKA_TOPIC_COVID_SUMMARY)

    def publish_summary(self, country_summary):
        logger.info(f"Publishing country stats: {country_summary}...")
        self.publish_message(country_summary)
