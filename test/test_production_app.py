from production.handover.api.endpoints.handover import *
import json
def test(client):

    "Test Case1: "
    # Make a tes call to /api
    response = client.get("api/")
    # Validate the response
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json == [{
    }]

