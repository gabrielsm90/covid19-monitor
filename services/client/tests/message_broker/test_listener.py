from services.client.application.message_broker.listener import CovidNewJobListener
from services.common.lib.config import Config


def test_create_listener():
    new_job_listener = CovidNewJobListener()
    assert hasattr(new_job_listener, "config")
    assert Config.KAFKA_BOOTSTRAP_SERVER in new_job_listener.config.get(
        "bootstrap_servers"
    )
    assert new_job_listener.config.get("group_id") == "api_client"