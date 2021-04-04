"""
Scheduler Service.

Keeps running and scheduling new Jobs
at each X minutes (configurable).
"""

import common.lib.log  # noqa F401 -> Initializes log handlers.
from services.scheduler.application.scheduler import NewJobScheduler


if __name__ == "__main__":
    NewJobScheduler().start()
