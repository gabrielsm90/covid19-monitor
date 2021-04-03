"""Test suite for the class LogWriter."""

import os
import shutil

from common.lib.config import Config
from services.logger.application.writer import LogWriter


def _reset_log_dir():
    """Recreate log dir."""
    try:
        shutil.rmtree(Config.LOG_DIR)
    except Exception:  # noqa S110 If dir does not exist.
        pass
    os.mkdir(Config.LOG_DIR)


def test_write_log():
    """Test message write to log."""
    _reset_log_dir()
    Config.LOG_FILE = "tmp.log"
    log_writer = LogWriter()
    log_writer.write_log("Test")
    log_file_path = os.path.join(Config.LOG_DIR, Config.LOG_FILE)
    assert os.path.exists(log_file_path)
    with open(log_file_path) as f:
        text = f.read().strip()
    assert text == "Test"
