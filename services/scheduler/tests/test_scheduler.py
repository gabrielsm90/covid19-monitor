"""Tests suite for NewJobScheduler."""

from apscheduler.schedulers.blocking import BlockingScheduler
import mock

from services.scheduler.application.scheduler import NewJobScheduler


def test_create_new_job_scheduler():
    """Test creation of a new scheduler."""
    scheduler = NewJobScheduler()
    assert isinstance(scheduler, BlockingScheduler)
    assert hasattr(scheduler, "new_job_producer")
    assert scheduler.new_job_producer is not None


@mock.patch(
    "services.scheduler.application.scheduler.BlockingScheduler.start",
    return_value=None,
)
def test_start_scheduler(mocked_start):
    """Test starting of new schedule."""
    scheduler = NewJobScheduler()
    scheduler.start()
    assert len(scheduler.get_jobs()) == 1
