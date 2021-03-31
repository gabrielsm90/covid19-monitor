"""

Covid 19 API Client.

This module defines a client to the Covid 19 public API.

"""

from typing import Any, Dict

import requests

from services.common.lib.config import Config


class CovidAPIClient:
    """
    Covid 19 API Client.

    Provides only one static method to fetch the
    /summary endpoint in the API.
    """

    @staticmethod
    def get_covid_summary() -> Dict[str, Any]:
        """
        Get Covid 19 stats summary.

        For reference: https://api.covid19api.com/summary

        Returns:
            Dict[str, Union[str, int]]: JSON with
                the statistics.
        """
        response = requests.get(Config.COVID_API_URL)
        response.raise_for_status()
        return response.json()
