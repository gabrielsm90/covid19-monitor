"""Tests suite for class KafkaCovidLogListener."""
import uuid

from common.lib.config import Config
from common.lib.communication.mom.brokers.kafkamq import CovidMonitorKafkaProducer
from services.logger.application.communication.factory import (
    CovidLogListenerFactory,
)


def test_create_log_kafka_listener():
    """Test creation of a new listener."""
    new_job_listener = CovidLogListenerFactory.get_log_listener("kafka")()
    assert hasattr(new_job_listener, "listener")
    assert hasattr(new_job_listener.listener, "config")
    assert Config.KAFKA["HOST"] in new_job_listener.listener.config.get(
        "bootstrap_servers"
    )
    assert new_job_listener.listener.config.get("group_id") == "logger"


def test_consume_log_kafka_listener():
    """Test consume message from Kafka."""
    test_topic = uuid.uuid4().hex
    Config.KAFKA["TOPIC_LOG"] = test_topic
    log_listener = CovidLogListenerFactory.get_log_listener("kafka")(
        auto_offset_reset="earliest"
    )
    producer = CovidMonitorKafkaProducer(test_topic)
    producer.publish_message({})
    for msg in log_listener.consume():
        assert msg == {}
        break
