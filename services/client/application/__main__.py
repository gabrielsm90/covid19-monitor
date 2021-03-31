"""

Covid 19 API Client.

This service is responsible for fetching the covid 19 stats API.

It's listening to the New Job queue and, as soon as a new job arrives,
fetches the API, formats the stats and publishes the result to the
Covid Summary queue.

"""
import logging

from services.client.application.covid_api_client import CovidAPIClient
from services.common.lib.config import Config
from services.common.lib.utils.covid_monitor_kafka import (
    CovidMonitorKafkaConsumer,
    CovidMonitorKafkaProducer,
)
import services.common.lib.utils.log  # noqa F401 -> Initializes log handlers.


logger = logging.getLogger(Config.LOG_NAME)


if __name__ == "__main__":
    covid_api_client = CovidAPIClient()
    new_covid_summary_producer = CovidMonitorKafkaProducer(
        topic=Config.KAFKA_TOPIC_COVID_SUMMARY
    )
    new_job_listener = CovidMonitorKafkaConsumer(
        topic=Config.KAFKA_TOPIC_SCHEDULER, group_id="api_client"
    )
    for _ in new_job_listener.consume():
        try:
            covid_summary = covid_api_client.get_covid_summary()
            for country_summary in covid_summary.get("Countries", []):
                logger.info(f"Publishing country stats: {country_summary}...")
                new_covid_summary_producer.publish_message(country_summary)
        except Exception:
            logger.exception("Failed to fetch Covid API")
