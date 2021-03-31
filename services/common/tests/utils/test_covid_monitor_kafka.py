import mock

from services.common.lib.config import Config
from services.common.lib.utils.covid_monitor_kafka import CovidMonitorKafkaProducer, CovidMonitorKafkaConsumer


def test_create_covid_monitor_kafka_consumer():
    consumer = CovidMonitorKafkaConsumer("topic", "group_id")
    assert hasattr(consumer, "config")
    assert Config.KAFKA_BOOTSTRAP_SERVER in consumer.config.get(
        "bootstrap_servers"
    )
    assert consumer.config.get("group_id") == "group_id"


def test_create_covid_monitor_kafka_producer():
    producer = CovidMonitorKafkaProducer("topic")
    assert hasattr(producer, "config")
    assert Config.KAFKA_BOOTSTRAP_SERVER in producer.config.get(
        "bootstrap_servers"
    )


@mock.patch("services.common.lib.utils.covid_monitor_kafka.logger.info")
def test_publish_message_to_covid_monitor_kafka(log_mock):
    producer = CovidMonitorKafkaProducer("topic")
    producer.publish_message({})
    log_mock.assert_called_once()


def test_consume_covid_monitor_kafka_consumer():
    consumer = CovidMonitorKafkaConsumer("topic", "group_id", auto_offset_reset="earliest")
    producer = CovidMonitorKafkaProducer("topic")
    producer.publish_message({})
    for msg in consumer.consume():
        assert msg == {}
        break
