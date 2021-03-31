"""
Flask application.

App which will provide a REST API
to update and consult the monitor
generated data.
"""

from flask import Flask

from services.server.application.controllers.countries import countries


def not_found_response(e):
    """Handle 404 errors."""
    return "Not Found", 404


# Creates the Flask app.
app = Flask(__name__)
app.register_blueprint(countries)
app.register_error_handler(404, not_found_response)
