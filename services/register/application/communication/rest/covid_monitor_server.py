"""Module to provide communication with the Covid 19 Monitor server."""
from typing import Any, Dict

import requests

from common.lib.config import Config


class CovidMonitorRestApiClient:
    """Client to the Covid 19 Monitor server service."""

    def __init__(self):
        """Create new client for Covid 19 Monitor server with the base url as attr."""
        self.base_url = Config.SERVER_URL

    def get_countries_url(self) -> str:
        """
        Get url for the endpoint /countries.

        Returns:
            str: Url for the endpoint /countries.
        """
        return f"{self.base_url}/countries"

    def get_country_url(self, country_code: str) -> str:
        """
        Get url for the endpoint /countries/<country_code>.

        Args:
            country_code (str): Country's code, such as MA.

        Returns:
            str: Url for the endpoint /countries/<country_code>.
        """
        return f"{self.get_countries_url()}/{country_code}"

    def post_summary(self, covid_summary: Dict[str, Any]):
        """
        Publish summary to Covid 19 Monitor Server.

        Args:
            covid_summary (Dict[str, Any]): Summary to be published.
        """
        country_url = self.get_country_url(covid_summary["country_code"])
        response = requests.get(country_url)
        if response.status_code == 404:
            requests.post(self.get_countries_url(), json=covid_summary)
            return
        if response.status_code == 200:
            requests.patch(country_url, json=covid_summary)
        response.raise_for_status()
