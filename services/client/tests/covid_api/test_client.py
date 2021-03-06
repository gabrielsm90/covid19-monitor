"""Tests suite for the CovidAPIClient class."""

import mock

from services.client.application.covid_api.client import CovidAPIClient


def test_get_covid_summary_with_success():
    """Test fetching summary with success."""
    response = CovidAPIClient.get_covid_summary()
    assert isinstance(response, dict)
    assert "Countries" in response
    assert isinstance(response["Countries"], list)
    for summary in response["Countries"]:
        assert summary.get("Country")
        assert summary.get("CountryCode")
        assert summary.get("NewConfirmed") is not None
        assert summary.get("TotalConfirmed") is not None
        assert summary.get("NewDeaths") is not None
        assert summary.get("TotalDeaths") is not None
        assert summary.get("NewRecovered") is not None
        assert summary.get("TotalRecovered") is not None


@mock.patch("services.client.application.covid_api.client.Config.COVID_API_URL")
@mock.patch("services.client.application.covid_api.client.logger.exception")
def test_get_covid_summary_with_error(
    log_mock: mock.MagicMock, api_url_mock: mock.MagicMock
):
    """
    Tests covid summary with error response.

    A fake url is provided to force the error.

    Args:
        log_mock (mock.MagicMock): Mock for logging.exception
            function. That function should be called once in
            this case.
        api_url_mock (mock.MagicMock): Mock for covid api in
            the configuration.
    """
    invalid_url = "http://localhost:101010/"
    api_url_mock.return_value = invalid_url
    response = CovidAPIClient.get_covid_summary()
    assert response is None
    log_mock.assert_called_once_with("Failed to fetch Covid API")
