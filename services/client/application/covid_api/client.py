"""

Covid 19 API Client.

This module defines a client to the Covid 19 public API.

"""
import logging
from typing import Any, Dict

import requests

from common.lib.config import Config


logger = logging.getLogger(Config.LOG_NAME)


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
        try:
            response = requests.get(Config.COVID_API_URL)
            response.raise_for_status()
            logger.info("Covid 19 summary fetched successfully")
            return response.json()
        except Exception:
            logger.exception("Failed to fetch Covid API")
