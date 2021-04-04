"""

Covid 19 API Client.

This service is responsible for fetching the covid 19 stats API.

It's listening to the New Job queue and, as soon as a new job arrives,
fetches the API, formats the stats and publishes the result to the
Covid Summary queue.

"""
from common.lib.config import Config
import common.lib.log  # noqa F401 -> Initializes log handlers.
from services.client.application.covid_api.client import CovidAPIClient
from services.client.application.communication.factory import (
    CovidSummaryPublisherFactory,
    NewJobListenerFactory,
)


if __name__ == "__main__":
    covid_api_client = CovidAPIClient()
    covid_summary_publisher = CovidSummaryPublisherFactory.get_covid_summary_publisher(
        Config.MESSAGE_QUEUE
    )()
    new_job_listener = NewJobListenerFactory.get_new_job_listener(
        Config.MESSAGE_QUEUE
    )()
    for _ in new_job_listener.consume():
        covid_summary = covid_api_client.get_covid_summary()
        if covid_summary:
            for country_summary in covid_summary.get("Countries", []):
                covid_summary_publisher.publish(country_summary)
