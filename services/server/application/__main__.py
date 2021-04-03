"""
Server service.

This service exposes a REST API
to update and consult the monitor
generated data.

This module starts the app.
"""

from mongoengine import connect

from common.lib.config import Config
import common.lib.utils.log  # noqa F401 -> Initializes log handlers.
from services.server.application.app import app


if __name__ == "__main__":
    conn = connect("covid19", host=Config.MONGO_HOST, port=27017)
    app.run(host="0.0.0.0")  # noqa S104 - App still made to run only locally.
