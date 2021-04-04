"""Module to provide factories for Summary listeners."""

from services.register.application.communication.mom.brokers.kafka import (
    KafkaCovidSummaryListener,
)


class CovidSummaryListenerFactory:
    """Covid summary Listener factory."""

    # Available concrete listeners.
    AVAILABLE_LISTENERS = {"kafka": KafkaCovidSummaryListener}

    @staticmethod
    def get_covid_summary_listener(listener_key: str) -> type:
        """
        Get concrete Covid Summary Listener class.

        Args:
            listener_key (str): Key for the concrete listener (e.g. "kafka")

        Returns:
            type: Covid Summary Listener concrete class.
        """
        return CovidSummaryListenerFactory.AVAILABLE_LISTENERS[listener_key]
