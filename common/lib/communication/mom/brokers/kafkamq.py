"""

Kafka module.

This module provides generics Consumer and Producer to
the Kafka MQ.

"""

import json
import logging
from typing import Any, Dict
import uuid

from kafka import KafkaConsumer, KafkaProducer

from common.lib.config import Config


logger = logging.getLogger(Config.LOG_NAME)


class CovidMonitorKafkaConsumer(KafkaConsumer):
    """Kafka message consumer."""

    def __init__(self, topic: str, group_id: str, auto_offset_reset: str = "latest"):
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
            auto_offset_reset(str): A policy for resetting offsets
                on OffsetOutOfRange errors: ‘earliest’ will move to
                the oldest available message, ‘latest’ will move to
                the most recent. Any other value will raise the exception.
                Default: ‘latest’.
        """
        super().__init__(
            topic,
            bootstrap_servers=[Config.KAFKA["HOST"]],
            enable_auto_commit=True,
            max_poll_records=1,
            group_id=group_id,
            api_version=(0, 10, 1),
            auto_offset_reset=auto_offset_reset,
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
            bootstrap_servers=[Config.KAFKA["HOST"]], api_version=(0, 10, 1)
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
        logger.info(
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
        self.send(value).add_callback(self._on_message_published, value).get()

    def send(self, value: Dict[str, Any], **kwargs):
        """
        Publish message to topic.

        Args:
            value (Dict[str, Any]): Message.
        """
        value = json.dumps(value).encode("utf-8")
        return super(CovidMonitorKafkaProducer, self).send(
            self.topic, key=uuid.uuid4().bytes, value=value
        )
