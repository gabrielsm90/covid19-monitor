"""Module to provide the log writer."""

import os

from common.lib.config import Config


class LogWriter:
    """Log Writer."""

    def __init__(self):
        """Create new log writer with a target file to write to."""
        self.target_file = os.path.join(Config.LOG_DIR, Config.LOG_FILE)

    def write_log(self, log_message: str):
        """
        Write message to log file.

        Args:
            log_message (str): Message to be written.
        """
        with open(self.target_file, "a") as log_file:
            log_file.write(f"{log_message}\n")
