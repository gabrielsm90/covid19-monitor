"""Tests suite for class kafka.NewJobPublisher."""

import mock

from services.scheduler.application.communication.factory import (
    NewJobPublisherFactory,
)
from common.lib.config import Config


def test_create_kafka_publisher():
    """Test create new publisher."""
    kafka_new_job_publisher = NewJobPublisherFactory.get_new_job_publisher("kafka")()
    assert hasattr(kafka_new_job_publisher, "publisher")
    assert hasattr(kafka_new_job_publisher.publisher, "config")
    assert Config.KAFKA["HOST"] in kafka_new_job_publisher.publisher.config.get(
        "bootstrap_servers"
    )


@mock.patch("services.client.application.communication.brokers.kafka.logger.info")
def test_kafka_publish_new_job(log_mock: mock.MagicMock):
    """
    Test publishing summary.

    Args:
        log_mock (mock.MagicMock): Mock for logging.info
            function. That function should be called twice
            in this case.
    """
    kafka_new_job_publisher = NewJobPublisherFactory.get_new_job_publisher("kafka")()
    kafka_new_job_publisher.publish()
    assert log_mock.call_count == 3  # Constructor, Publishing and Published
