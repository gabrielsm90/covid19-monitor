import mock

from services.client.application.message_broker.publisher import CovidSummaryPublisher
from services.common.lib.config import Config


def test_create_publisher():
    summary_publisher = CovidSummaryPublisher()
    assert hasattr(summary_publisher, "config")
    assert Config.KAFKA_BOOTSTRAP_SERVER in summary_publisher.config.get(
        "bootstrap_servers"
    )


@mock.patch("services.client.application.message_broker.publisher.logger.info")
def test_publish_summary(log_mock):
    summary_publisher = CovidSummaryPublisher()
    summary_publisher.publish_summary({})
    assert log_mock.call_count == 2  # Publishing and Published
