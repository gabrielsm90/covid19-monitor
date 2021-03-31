"""

Kafka module.

This module provides generics Consumer and Producer to
the Kafka MQ.

"""

import json
import uuid

from kafka import KafkaConsumer, KafkaProducer

from services.common.lib.config import Config


class CovidMonitorKafkaConsumer(KafkaConsumer):
    """Kafka message consumer."""

    def __init__(self, topic: str, group_id: str):
        """
        Create new consumer with provided configuration.

        Args:
            topic (str): Topic on which this consumer
                will be listening.
            group_id (str): Kafka Group id for the
                consumer. More info on
                https://jaceklaskowski.gitbooks.io/
                apache-kafka/content/
                kafka-properties-group-id.html
        """
        super().__init__(
            topic,
            bootstrap_servers=[Config.KAFKA_BOOTSTRAP_SERVER],
            enable_auto_commit=True,
            max_poll_records=1,
            group_id=group_id,
            api_version=(0, 10, 1),
        )

    def consume(self):
        """
        Consume topic.

        Method that keeps running and monitoring
        new messages. Once a message is obtained,
        it's yield to whoever is using this consumer.
        """
        for msg in self:
            yield json.loads(msg.value.decode("utf-8"))


class CovidMonitorKafkaProducer(KafkaProducer):
    """Kafka message producer."""

    def __init__(self, topic: str):
        """
        Produce messages to topic.

        Args:
            topic (str): Topic where this
                producer will write.
        """
        self.topic = topic
        super().__init__(
            bootstrap_servers=[Config.KAFKA_BOOTSTRAP_SERVER], api_version=(0, 10, 1)
        )

    @staticmethod
    def _on_message_published(body: bytes, record_metadata):
        """
        Log message published.

        This is a callback function to when a message
        is published by this consumer that only logs
        a general result of the posted message.

        Args:
            body (bytes): Message's body.
            record_metadata: Record's metadata
                with info such as the topic and
                the message's offset.
        """
        print(
            f"Message {record_metadata.offset} published "
            f"successfully in topic {record_metadata.topic}. "
            f"Body: {body}"
        )

    def publish_message(self, value: dict):
        """
        Publish message to topic.

        Args:
            value (dict): Content to be published.
        """
        value = json.dumps(value).encode("utf-8")
        self.send(self.topic, key=uuid.uuid4().bytes, value=value).add_callback(
            self._on_message_published, value
        ).get()
