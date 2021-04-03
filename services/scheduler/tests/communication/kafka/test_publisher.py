"""Tests suite for class NewJobPublisher."""

import mock

from services.scheduler.application.communication.kafka.publisher import (
    NewJobPublisher,
)
from common.lib.config import Config


def test_create_publisher():
    """Test create new publisher."""
    summary_publisher = NewJobPublisher()
    assert hasattr(summary_publisher, "config")
    assert Config.KAFKA_BOOTSTRAP_SERVER in summary_publisher.config.get(
        "bootstrap_servers"
    )


@mock.patch("services.client.application.communication.kafka.publisher.logger.info")
def test_publish_new_job(log_mock: mock.MagicMock):
    """
    Test publishing summary.

    Args:
        log_mock (mock.MagicMock): Mock for logging.info
            function. That function should be called twice
            in this case.
    """
    summary_publisher = NewJobPublisher()
    summary_publisher.publish_new_job()
    assert log_mock.call_count == 3  # Constructor, Publishing and Published
