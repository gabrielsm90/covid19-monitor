"""Test suite for class CovidMonitorRestApiClient."""

from typing import Dict, Union
import uuid

import mock
import pytest

from common.lib.config import Config
from services.register.application.communication.rest.covid_monitor_server import (
    CovidMonitorRestApiClient,
)


@pytest.fixture
def summary_message():
    """Fixture with a summary message example."""
    return {
        "country": "Brazil",
        "country_code": "BR",
        "new_confirmed": 10,
        "total_confirmed": 100,
        "new_deaths": 1,
        "total_deaths": 50,
        "new_recovered": 2,
        "total_recovered": 70,
    }


@pytest.fixture(scope="session")
def covid_monitor_rest_client():
    """Fixture with a Covid Monitor REST API client."""
    return CovidMonitorRestApiClient()


def test_get_country_url(covid_monitor_rest_client: CovidMonitorRestApiClient):
    """
    Test function get_country.

    Args:
        covid_monitor_rest_client (CovidMonitorRestApiClient): Covid
            Monitor REST API client.
    """
    country_url = covid_monitor_rest_client.get_country_url("XX")
    assert country_url == f"{Config.SERVER_URL}/countries/XX"


def test_get_countries_url(covid_monitor_rest_client: CovidMonitorRestApiClient):
    """
    Test function get_countries.

    Args:
        covid_monitor_rest_client (CovidMonitorRestApiClient): Covid
            Monitor REST API client.
    """
    countries_url = covid_monitor_rest_client.get_countries_url()
    assert countries_url == f"{Config.SERVER_URL}/countries"


@mock.patch(
    "services.register.application.communication.rest."
    "covid_monitor_server.requests.patch"
)
def test_post_new_country_summary(
    patch_mock: mock.MagicMock,
    covid_monitor_rest_client: CovidMonitorRestApiClient,
    summary_message: Dict[str, Union[str, int]],
):
    """
    Test publishing of new summary.

    Args:
        patch_mock (mock.MagicMock): Mocked requests.patch.
        covid_monitor_rest_client (CovidMonitorRestApiClient): Covid
            Monitor REST API client.
        summary_message (Dict[str, Union[str, int]]): Summary message
            example.
    """
    summary_message["country_code"] = uuid.uuid4().hex
    covid_monitor_rest_client.post_summary(summary_message)
    patch_mock.assert_not_called()


@mock.patch(
    "services.register.application.communication.rest."
    "covid_monitor_server.requests.patch"
)
def test_post_existent_country_summary(
    patch_mock: mock.MagicMock,
    covid_monitor_rest_client: CovidMonitorRestApiClient,
    summary_message: Dict[str, Union[str, int]],
):
    """
    Test publishing summary to a county already in the base.

    Args:
        patch_mock (mock.MagicMock): Mocked requests.patch.
        covid_monitor_rest_client (CovidMonitorRestApiClient): Covid
            Monitor REST API client.
        summary_message (Dict[str, Union[str, int]]): Summary message
            example.
    """
    country_code = uuid.uuid4().hex
    summary_message["country_code"] = country_code
    covid_monitor_rest_client.post_summary(summary_message)
    covid_monitor_rest_client.post_summary(summary_message)
    patch_mock.assert_called()
