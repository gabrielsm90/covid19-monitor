"""

Covid 19 API Client.

This service is responsible for fetching the covid 19 stats API.

It's listening to the New Job queue and, as soon as a new job arrives,
fetches the API, formats the stats and publishes the result to the
Covid Summary queue.

"""

from services.client.application.covid_api.client import CovidAPIClient
from services.client.application.message_broker.listener import CovidNewJobListener
from services.client.application.message_broker.publisher import CovidSummaryPublisher


if __name__ == "__main__":
    covid_api_client = CovidAPIClient()
    publisher = CovidSummaryPublisher()
    new_job_listener = CovidNewJobListener()
    for _ in new_job_listener.consume():
        covid_summary = covid_api_client.get_covid_summary()
        if covid_summary:
            for country_summary in covid_summary.get("Countries", []):
                publisher.publish_summary(country_summary)
