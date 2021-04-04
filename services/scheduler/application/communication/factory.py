"""Module to provide a New Job Publisher factory."""

from services.scheduler.application.communication.brokers.kafka import (
    KafkaNewJobPublisher,
)


class NewJobPublisherFactory:
    """New Job Publisher factory."""

    # Available concrete publishers.
    AVAILABLE_PUBLISHERS = {"kafka": KafkaNewJobPublisher}

    @staticmethod
    def get_new_job_publisher(publisher_key: str) -> type:
        """
        Get concrete New Job Publisher class.

        Args:
            publisher_key (str): Key for the concrete publisher (e.g. "kafka")

        Returns:
            type: New Job Publisher concrete class.
        """
        return NewJobPublisherFactory.AVAILABLE_PUBLISHERS[publisher_key]
