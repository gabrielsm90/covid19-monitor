from abc import ABCMeta, abstractmethod
from typing import Any, Dict


class Listener(metaclass=ABCMeta):
    """Message Queue Listener."""

    @abstractmethod
    def __init__(self, listener: Any):
        """
        Create new Message Queue listener.

        New listener is created with a provided
        Message Broker communication object.

        Args:
            listener (Any): Object that communicates
                with a message broker.
        """
        self.listener = listener  # pragma: no cover

    @abstractmethod
    def consume(self):
        """Consume messages from Message Broker."""
        raise NotImplementedError


class Publisher(metaclass=ABCMeta):
    """Message publisher."""

    @abstractmethod
    def __init__(self, publisher: Any):
        """
        Create new Covid Summary producer.

        Args:
            publisher (Any): Object that communicates
                with a message broker.
        """
        self.publisher = publisher  # pragma: no cover

    @abstractmethod
    def publish(self, message: Dict[str, Any]):
        """
        Publish message to message broker.

        Args:
            message (Dict[str, Any]): Message to
                be published.
        """
        raise NotImplementedError
