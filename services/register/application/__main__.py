"""
Register service.

Keeps listening to new results published by the
Client service and persists them by using the API
exposed by the Server service.
"""

from common.lib.config import Config
import common.lib.log  # noqa F401 -> Initializes log handlers.
from services.register.application.communication.mom.factory import (
    CovidSummaryListenerFactory,
)
from services.register.application.communication.rest.covid_monitor_server import (
    CovidMonitorRestApiClient,
)


if __name__ == "__main__":
    covid19_monitor_rest_client = CovidMonitorRestApiClient()
    new_summary_listener = CovidSummaryListenerFactory.get_covid_summary_listener(
        Config.MESSAGE_QUEUE
    )()
    for summary_message in new_summary_listener.consume():
        covid19_monitor_rest_client.post_summary(summary_message)
