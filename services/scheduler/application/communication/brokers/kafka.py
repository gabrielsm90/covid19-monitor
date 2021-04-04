"""Module to provide communication with Kafka."""

import logging
import uuid

from common.lib.config import Config
from common.lib.communication.mom import Publisher
from common.lib.communication.mom.brokers.kafkamq import CovidMonitorKafkaProducer


logger = logging.getLogger(Config.LOG_NAME)


class KafkaNewJobPublisher(Publisher):
    """Class that publishes new job to a topic in Kafka Message Broker."""

    def __init__(self):
        """Create new publisher that writes to a scheduler topic."""
        super().__init__(
            CovidMonitorKafkaProducer(topic=Config.KAFKA["TOPIC_SCHEDULER"])
        )
        logger.info(
            "New jobs scheduled at Kafka Server "
            f"{self.publisher.config['bootstrap_servers']} "
            f"- Topic {Config.KAFKA['TOPIC_SCHEDULER']}"
        )

    def publish(self, **kwargs):
        """Publish new job to message broker."""
        job_id = uuid.uuid4().hex
        logger.info(f"Publishing new job with job_id {job_id}...")
        self.publisher.publish_message({"job_id": job_id})
