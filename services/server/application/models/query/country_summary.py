"""
Layer used to query model objects.

Used by the app's controllers, it provides
operations to handle the data.
"""

from datetime import datetime
import json

from services.server.application.models.country_summary import CountrySummary


def create_country(country_summary: dict):
    """
    Create new country summary.

    Args:
        country_summary (dict): Summary's data.
    """
    country_summary = CountrySummary(**country_summary)
    country_summary.created_at = datetime.now()
    country_summary.save()


def get_countries():
    """
    Fetch all countries' covid summary.

    Returns:
        JSON with all summaries.
    """
    response = CountrySummary.objects()
    return json.loads(response.to_json())


def get_country(country_code: str, return_object: bool = False):
    """
    Fetch single country by its code.

    Args:
        country_code (str): Country's code such as
            UK or US.
        return_object (bool): Flag defining if an
            object should be returned or a json.

    Returns:
        Country's summary.
    """
    try:
        response = CountrySummary.objects.get(country_code=country_code)
    except CountrySummary.DoesNotExist:
        return None
    if return_object:
        return response
    return json.loads(response.to_json())


def update_country(country_code, **kwargs):
    """
    Update single country.

    Updates a country summary with info passed
    in the kwargs.

    Args:
        country_code (str): Country's code such as
            UK or US.
    """
    country_summary = get_country(country_code, return_object=True)
    for field, new_value in kwargs.items():
        setattr(country_summary, field, new_value)
    country_summary.save()
