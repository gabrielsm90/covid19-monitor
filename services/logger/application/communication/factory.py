"""Module to provide a factory for Log listeners."""

from services.logger.application.communication.brokers.kafka import (
    KafkaCovidLogListener,
)


class CovidLogListenerFactory:
    """Log Listener factory."""

    # Available concrete listeners.
    AVAILABLE_LISTENERS = {"kafka": KafkaCovidLogListener}

    @staticmethod
    def get_log_listener(listener_key: str) -> type:
        """
        Get concrete Log Listener class.

        Args:
            listener_key (str): Key for the concrete listener (e.g. "kafka")

        Returns:
            type: Log Listener concrete class.
        """
        return CovidLogListenerFactory.AVAILABLE_LISTENERS[listener_key]
