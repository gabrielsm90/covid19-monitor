"""Tests suite for class CovidLogListener."""

from services.logger.application.communication.kafka.listener import (
    CovidLogListener,
)
from common.lib.config import Config


def test_create_listener():
    """Test creation of a new listener."""
    new_job_listener = CovidLogListener()
    assert hasattr(new_job_listener, "config")
    assert Config.KAFKA_BOOTSTRAP_SERVER in new_job_listener.config.get(
        "bootstrap_servers"
    )
    assert new_job_listener.config.get("group_id") == "logger"
