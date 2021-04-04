"""Tests suite for communication with Kafka."""
import uuid

import mock

from services.client.application.communication.factory import (
    NewJobListenerFactory,
    CovidSummaryPublisherFactory,
)
from common.lib.config import Config
from common.lib.communication.mom.brokers.kafkamq import CovidMonitorKafkaProducer


def test_create_kafka_new_job_listener():
    """Test creation of a new job listener in Kafka."""
    new_job_listener = NewJobListenerFactory.get_new_job_listener("kafka")()
    assert hasattr(new_job_listener, "listener")
    assert hasattr(new_job_listener.listener, "config")
    assert Config.KAFKA["HOST"] in new_job_listener.listener.config.get(
        "bootstrap_servers"
    )
    assert new_job_listener.listener.config.get("group_id") == "api_client"


def test_create_kafka_covid_summary_publisher():
    """Test create new kafka summary publisher."""
    summary_publisher = CovidSummaryPublisherFactory.get_covid_summary_publisher(
        "kafka"
    )()
    assert hasattr(summary_publisher, "publisher")
    assert hasattr(summary_publisher.publisher, "config")
    assert Config.KAFKA["HOST"] in summary_publisher.publisher.config.get(
        "bootstrap_servers"
    )


@mock.patch("services.client.application.communication.brokers.kafka.logger.info")
def test_publish_covid_summary_to_kafka(log_mock: mock.MagicMock):
    """
    Test publishing summary.

    Args:
        log_mock (mock.MagicMock): Mock for logging.info
            function. That function should be called twice
            in this case.
    """
    summary_publisher = CovidSummaryPublisherFactory.get_covid_summary_publisher(
        "kafka"
    )()
    summary_publisher.publish({})
    assert log_mock.call_count == 2  # Publishing and Published


def test_consume_new_job_kafka_listener():
    """Test consume message from Kafka."""
    test_topic = uuid.uuid4().hex
    Config.KAFKA["TOPIC_SCHEDULER"] = test_topic
    new_job_listener = NewJobListenerFactory.get_new_job_listener("kafka")(
        auto_offset_reset="earliest"
    )
    producer = CovidMonitorKafkaProducer(test_topic)
    producer.publish_message({})
    for msg in new_job_listener.consume():
        assert msg == {}
        break
