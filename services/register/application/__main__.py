"""
Register service.

Keeps listening to new results published by the
Client service and persists them by using the API
exposed by the Server service.
"""

import common.lib.utils.log  # noqa F401 -> Initializes log handlers.
from services.register.application.communication.kafka.listener import (
    CovidSummaryConsumer,
)
from services.register.application.communication.rest.covid_monitor_server import (
    CovidMonitorRestApiClient,
)


if __name__ == "__main__":
    covid19_monitor_rest_client = CovidMonitorRestApiClient()
    new_summary_listener = CovidSummaryConsumer()
    for summary_message in new_summary_listener.consume():
        covid19_monitor_rest_client.post_summary(summary_message)
