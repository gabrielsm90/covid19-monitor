"""Module to provide factories for New Job listeners and Summary publishers."""

from services.client.application.communication.brokers.kafka import (
    KafkaNewJobListener,
    KafkaCovidSummaryPublisher,
)


class NewJobListenerFactory:
    """New Job Listener factory."""

    # Available concrete listeners.
    AVAILABLE_LISTENERS = {"kafka": KafkaNewJobListener}

    @staticmethod
    def get_new_job_listener(listener_key: str) -> type:
        """
        Get concrete New Job Listener class.

        Args:
            listener_key (str): Key for the concrete listener (e.g. "kafka")

        Returns:
            type: New Job Listener concrete class.
        """
        return NewJobListenerFactory.AVAILABLE_LISTENERS[listener_key]


class CovidSummaryPublisherFactory:
    """Covid Summary Publisher factory."""

    # Available concrete publishers.
    AVAILABLE_PUBLISHERS = {"kafka": KafkaCovidSummaryPublisher}

    @staticmethod
    def get_covid_summary_publisher(listener_key: str) -> type:
        """
        Get concrete New Job Listener class.

        Args:
            listener_key (str): Key for the concrete publisher (e.g. "kafka")

        Returns:
            type: New Job Listener concrete class.
        """
        return CovidSummaryPublisherFactory.AVAILABLE_PUBLISHERS[listener_key]
