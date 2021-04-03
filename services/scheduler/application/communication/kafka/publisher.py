"""Module to provide a new job publisher."""

import logging
import uuid

from common.lib.config import Config
from common.lib.utils.covid_monitor_kafka import CovidMonitorKafkaProducer


logger = logging.getLogger(Config.LOG_NAME)


class NewJobPublisher(CovidMonitorKafkaProducer):
    """Class that publishes new job to message broker."""

    def __init__(self):
        """Create new publisher that writes to a scheduler topic."""
        super().__init__(topic=Config.KAFKA_TOPIC_SCHEDULER)
        logger.info(
            f"New jobs being scheduled at server "
            f"New jobs scheduled at: {self.config['bootstrap_servers']} "
            f"- Topic {Config.KAFKA_TOPIC_SCHEDULER}"
        )

    def publish_new_job(self):
        """Publish new job to message broker."""
        job_id = uuid.uuid4().hex
        logger.info(f"Publishing new job with job_id {job_id}...")
        self.publish_message({"job_id": job_id})
