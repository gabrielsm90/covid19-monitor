"""Tests suite for class CovidLogListener."""
import uuid

from common.lib.config import Config
from common.lib.utils.covid_monitor_kafka import CovidMonitorKafkaProducer
from services.register.application.communication.kafka.listener import (
    CovidSummaryConsumer,
)


def test_create_listener():
    """Test creation of a new listener."""
    new_job_listener = CovidSummaryConsumer()
    assert hasattr(new_job_listener, "config")
    assert Config.KAFKA_BOOTSTRAP_SERVER in new_job_listener.config.get(
        "bootstrap_servers"
    )
    assert new_job_listener.config.get("group_id") == "job_scheduler"


def test_consume_covid_monitor_kafka_consumer():
    """Test consume message from Kafka."""
    topic = uuid.uuid4().hex
    Config.KAFKA_TOPIC_COVID_SUMMARY = topic
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
    consumer = CovidSummaryConsumer(auto_offset_reset="earliest")
    producer = CovidMonitorKafkaProducer(topic)
    producer.publish_message(message)
    for msg in consumer.consume():
        assert msg["country_code"] == "AL"
        break
