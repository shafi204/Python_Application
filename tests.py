import pytest
from logging import IncidentLogger

@pytest.fixture
def logger():
    # Create an instance of the IncidentLogger class with MongoDB connection details
    return IncidentLogger("mongodb://localhost:27017/", "incident_logs", "incidents")

def test_log_incident(logger):
    # Test logging an incident
    title = "Test Incident"
    description = "This is a test incident"

    logger.log_incident(title, description)

    # Assert that the incident is successfully logged
    assert logger.is_incident_logged(title, description) is True
