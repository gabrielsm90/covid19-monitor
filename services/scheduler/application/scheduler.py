"""
Module to define the main class of the scheduler service.

Keeps running and scheduling new Jobs
at each X minutes (configurable).
"""

from datetime import datetime
import logging
import uuid

from apscheduler.schedulers.blocking import BlockingScheduler

from services.common.lib.config import Config
from services.common.lib.utils.covid_monitor_kafka import CovidMonitorKafkaProducer


logger = logging.getLogger(Config.LOG_NAME)


class NewJobScheduler(BlockingScheduler):
    """New Job scheduler."""

    def __init__(self):
        """
        Build new scheduler.

        The Job Scheduler will keep running and
        scheduling new jobs in the configured
        topic.

        A new job will trigger the api client
        service.
        """
        super().__init__()
        self.new_job_producer = CovidMonitorKafkaProducer(
            topic=Config.KAFKA_TOPIC_SCHEDULER
        )
        logger.info(
            f"New jobs scheduled at: {Config.KAFKA_BOOTSTRAP_SERVER} "
            f"- Topic {Config.KAFKA_TOPIC_SCHEDULER}"
        )

    def start(self):
        """Start scheduler."""
        self.add_job(
            self.new_job_producer.publish_message,
            trigger="interval",
            args=({"job_id": uuid.uuid4().hex},),
            minutes=Config.NEW_JOB_INTERVAL,
            next_run_time=datetime.now(),
        )
        super().start()
