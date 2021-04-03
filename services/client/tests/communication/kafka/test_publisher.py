"""Tests suite for class CovidSummaryPublisher."""

import mock

from services.client.application.communication.kafka.publisher import (
    CovidSummaryPublisher,
)
from common.lib.config import Config


def test_create_publisher():
    """Test create new publisher."""
    summary_publisher = CovidSummaryPublisher()
    assert hasattr(summary_publisher, "config")
    assert Config.KAFKA_BOOTSTRAP_SERVER in summary_publisher.config.get(
        "bootstrap_servers"
    )


@mock.patch("services.client.application.communication.kafka.publisher.logger.info")
def test_publish_summary(log_mock: mock.MagicMock):
    """
    Test publishing summary.

    Args:
        log_mock (mock.MagicMock): Mock for logging.info
            function. That function should be called twice
            in this case.
    """
    summary_publisher = CovidSummaryPublisher()
    summary_publisher.publish_summary({})
    assert log_mock.call_count == 2  # Publishing and Published
