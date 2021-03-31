"""
Register service.

Keeps listening to new results published by the
Client service and persists them by using the API
exposed by the Server service.
"""

import requests

from services.common.lib.config import Config
from services.common.lib.utils.covid_monitor_kafka import (
    CovidMonitorKafkaConsumer,
    CovidMonitorKafkaProducer,
)


if __name__ == "__main__":
    new_covid_summary_producer = CovidMonitorKafkaProducer(
        topic=Config.KAFKA_TOPIC_COVID_SUMMARY
    )
    new_result_listener = CovidMonitorKafkaConsumer(
        topic=Config.KAFKA_TOPIC_COVID_SUMMARY, group_id="job_scheduler"
    )
    for new_job_message in new_result_listener.consume():
        covid_summary = {
            "country": new_job_message["Country"],
            "country_code": new_job_message["CountryCode"],
            "new_confirmed": new_job_message["NewConfirmed"],
            "total_confirmed": new_job_message["TotalConfirmed"],
            "new_deaths": new_job_message["NewDeaths"],
            "total_deaths": new_job_message["TotalDeaths"],
            "new_recovered": new_job_message["NewRecovered"],
            "total_recovered": new_job_message["TotalRecovered"],
        }
        countries_url = f"{Config.SERVER_URL}/countries"
        country_url = f"{countries_url}/{covid_summary['country_code']}"
        response = requests.get(country_url)
        if response.status_code == 404:
            requests.post(countries_url, json=covid_summary)
        elif response.status_code == 200:
            requests.patch(country_url, json=covid_summary)
        else:
            response.raise_for_status()
