"""
App's controllers.

Module to define the application's
controllers through Flask Blueprints.
"""

from flask import Blueprint, abort, request, jsonify

from services.server.application.models.query.country_summary import (
    create_country,
    get_countries,
    get_country,
    update_country,
)


countries = Blueprint("countries", __name__, url_prefix="/countries")


@countries.route("/")
def get():
    """
    Get all countries` covid case summary.

    Returns:
        Response to be sent to the client.
    """
    fetched_countries = get_countries()
    if fetched_countries:
        return jsonify(fetched_countries)
    return "No countries registered"


@countries.route("/<country_code>")
def get_one(country_code: str):
    """
    Get one country's covid case summary.

    Args:
        country_code (str): Country's code such as
            UK or BR.

    Returns:
        Response to be sent to the client.
    """
    country = get_country(country_code)
    if country:
        return country
    abort(404)


@countries.route("/<country_code>", methods=("PATCH",))
def update_one(country_code: str):
    """
    Update country's covid summary record.

    Args:
        country_code (str): Country's code such as
            UK or BR.

    Returns:
        Response to be sent to the client.
    """
    data = request.json
    update_country(**data)
    return "Country Updated", 200


@countries.route("/", methods=("POST",))
def create_one():
    """
    Create country's covid summary record.

    Returns:
        Response to be sent to the client.
    """
    data = request.json
    create_country(data)
    return "Country Summary Created", 201
