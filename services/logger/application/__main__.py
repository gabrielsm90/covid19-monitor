"""
Logger service.

Keeps listening to the messages that arrive
in the Log topic and writes them to a configured
file.
"""

from common.lib.config import Config
from services.logger.application.communication.factory import CovidLogListenerFactory
from services.logger.application.writer import LogWriter


if __name__ == "__main__":
    log_listener = CovidLogListenerFactory.get_log_listener(Config.MESSAGE_QUEUE)()
    log_writer = LogWriter()
    for message in log_listener.consume():
        log_writer.write_log(f"{message}\n")
