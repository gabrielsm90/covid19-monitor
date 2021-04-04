"""Countries endpoint test suite."""

from typing import Dict, Union

from flask.testing import FlaskClient
from mongoengine import connect
import pytest

from common.lib.config import Config
from services.server.application.app import app


conn = connect("covid19-tests", host=Config.MONGO_HOST, port=27017)


def clean_database():
    """Drop database to ensure clean environment."""
    conn.drop_database("covid19-tests")


@pytest.fixture
def country_summary() -> Dict[str, Union[str, int]]:
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
def app_test_client() -> FlaskClient:
    """Client for the Flask APP."""
    with app.test_client() as client:
        yield client


def test_get_countries_successful_response(
    app_test_client: FlaskClient, country_summary: Dict[str, Union[str, int]]
):
    """
    Test fetching all countries with successful response.

    Args:
        app_test_client (FlaskClient): App's HTTP client.
        country_summary (Dict[str, Union[str, int]]): Summary message example.
    """
    clean_database()
    app_test_client.post("countries/", json=country_summary)
    response = app_test_client.get("countries/")
    assert response.status_code == 200
    assert len(response.json) == 1


def test_get_countries_no_countries_response(app_test_client: FlaskClient):
    """
    Test fetching all countries with no countries registered.

    Args:
        app_test_client (FlaskClient): App's HTTP client.
    """
    clean_database()
    response = app_test_client.get("countries/")
    assert response.status_code == 200
    assert response.get_data().decode() == "No countries registered"


def test_get_one_country_successful_response(
    app_test_client: FlaskClient, country_summary: Dict[str, Union[str, int]]
):
    """
    Test fetching one country with no countries registered.

    Args:
        app_test_client (FlaskClient): App's HTTP client.
        country_summary (Dict[str, Union[str, int]]): Summary message example.
    """
    clean_database()
    app_test_client.post("countries/", json=country_summary)
    response = app_test_client.get(f"countries/{country_summary['country_code']}")
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert response.json["country_code"] == country_summary["country_code"]


def test_get_one_country_not_found_response(app_test_client: FlaskClient):
    """
    Test fetching one country with country not registered.

    Args:
        app_test_client (FlaskClient): App's HTTP client.
    """
    clean_database()
    response = app_test_client.get("countries/ZZ")
    assert response.status_code == 404
    assert response.get_data().decode() == "Not Found"


def test_post_country_successful_response(
    app_test_client: FlaskClient, country_summary: Dict[str, Union[str, int]]
):
    """
    Test posting one country with success.

    Args:
        app_test_client (FlaskClient): App's HTTP client.
        country_summary (Dict[str, Union[str, int]]): Summary message example.
    """
    clean_database()
    response = app_test_client.post("countries/", json=country_summary)
    assert response.status_code == 201
    assert response.get_data().decode() == "Country Summary Created"


def test_post_repeated_country(
    app_test_client: FlaskClient, country_summary: Dict[str, Union[str, int]]
):
    """
    Test posting repeated country.

    Args:
        app_test_client (FlaskClient): App's HTTP client.
        country_summary (Dict[str, Union[str, int]]): Summary message example.
    """
    clean_database()
    app_test_client.post("countries/", json=country_summary)
    response = app_test_client.post("countries/", json=country_summary)
    assert response.status_code == 400
    assert response.get_data().decode() == "Country already exists."


def test_update_country_successful_response(
    app_test_client: FlaskClient, country_summary: Dict[str, Union[str, int]]
):
    """
    Test updating one country with success.

    Args:
        app_test_client (FlaskClient): App's HTTP client.
        country_summary (Dict[str, Union[str, int]]): Summary message example.
    """
    clean_database()

    original_new_confirmed_number = country_summary["new_confirmed"]
    updated_new_confirmed_number = country_summary["new_confirmed"] + 100

    app_test_client.post("countries/", json=country_summary)

    pre_update_get_response = app_test_client.get(
        f"countries/{country_summary['country_code']}"
    )
    assert (
        pre_update_get_response.json["new_confirmed"] == original_new_confirmed_number
    )

    country_summary["new_confirmed"] = updated_new_confirmed_number
    response = app_test_client.patch(
        f"/countries/{country_summary['country_code']}", json=country_summary
    )
    assert response.status_code == 200

    post_update_get_response = app_test_client.get(
        f"countries/{country_summary['country_code']}"
    )
    assert (
        post_update_get_response.json["new_confirmed"] == updated_new_confirmed_number
    )
