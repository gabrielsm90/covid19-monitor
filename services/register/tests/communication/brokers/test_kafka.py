"""Tests suite for class CovidLogListener."""
import uuid

from common.lib.config import Config
from common.lib.communication.mom.brokers.kafkamq import CovidMonitorKafkaProducer
from services.register.application.communication.mom.factory import (
    CovidSummaryListenerFactory,
)


def test_create_covid_summary_kafka_listener():
    """Test creation of a new covid summary kafka listener."""
    covid_summary_listener = CovidSummaryListenerFactory.get_covid_summary_listener(
        "kafka"
    )()
    assert hasattr(covid_summary_listener, "listener")
    assert hasattr(covid_summary_listener.listener, "config")
    assert Config.KAFKA["HOST"] in covid_summary_listener.listener.config.get(
        "bootstrap_servers"
    )
    assert covid_summary_listener.listener.config.get("group_id") == "job_scheduler"


def test_consume_covid_monitor_kafka_consumer():
    """Test consume message from Kafka."""
    topic = uuid.uuid4().hex
    Config.KAFKA["TOPIC_COVID_SUMMARY"] = topic
    message = {
        "ID": "1217571a-62e3-415f-ac3e-a731d5893d89",
        "Country": "Albania",
        "CountryCode": "AL",
        "Slug": "albania",
        "NewConfirmed": 0,
        "TotalConfirmed": 125506,
        "NewDeaths": 0,
        "TotalDeaths": 2241,
        "NewRecovered": 0,
        "TotalRecovered": 91875,
        "Date": "2021-04-02T21:26:09.704Z",
        "Premium": {},
    }
    covid_summary_listener = CovidSummaryListenerFactory.get_covid_summary_listener(
        "kafka"
    )(auto_offset_reset="earliest")
    producer = CovidMonitorKafkaProducer(topic)
    producer.publish_message(message)
    for msg in covid_summary_listener.consume():
        assert msg["country_code"] == "AL"
        break
