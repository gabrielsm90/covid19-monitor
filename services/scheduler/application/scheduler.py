"""
Module to define the main class of the scheduler service.

Keeps running and scheduling new Jobs
at each X minutes (configurable).
"""

from datetime import datetime
import logging

from apscheduler.schedulers.blocking import BlockingScheduler

from common.lib.config import Config
from services.scheduler.application.communication.factory import NewJobPublisherFactory


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
        self.new_job_producer = NewJobPublisherFactory.get_new_job_publisher(
            Config.MESSAGE_QUEUE
        )()

    def start(self):
        """Start scheduler."""
        self.add_job(
            self.new_job_producer.publish,
            trigger="interval",
            minutes=Config.NEW_JOB_INTERVAL,
            next_run_time=datetime.now(),
        )
        super().start()
