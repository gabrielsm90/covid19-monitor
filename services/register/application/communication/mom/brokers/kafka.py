"""Module to provide a Kafka listener of new summaries."""

from common.lib.config import Config
from common.lib.communication.mom import Listener
from common.lib.communication.mom.brokers.kafkamq import CovidMonitorKafkaConsumer


class KafkaCovidSummaryListener(Listener):
    """Covid Summary consumer."""

    def __init__(self, **kwargs):
        """Create new Summary consumer with data from config."""
        super().__init__(
            CovidMonitorKafkaConsumer(
                topic=Config.KAFKA["TOPIC_COVID_SUMMARY"],
                group_id="job_scheduler",
                **kwargs
            )
        )

    def consume(self):
        """Consume messages from queue. Yields formatted messages."""
        for summary_message in self.listener.consume():
            covid_summary = {
                "country": summary_message["Country"],
                "country_code": summary_message["CountryCode"],
                "new_confirmed": summary_message["NewConfirmed"],
                "total_confirmed": summary_message["TotalConfirmed"],
                "new_deaths": summary_message["NewDeaths"],
                "total_deaths": summary_message["TotalDeaths"],
                "new_recovered": summary_message["NewRecovered"],
                "total_recovered": summary_message["TotalRecovered"],
            }
            yield covid_summary
