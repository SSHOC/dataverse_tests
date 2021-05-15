import os

import pytest

from ..conftest import read_json
from ..conftest import TEST_CONFIG_DATA_DIR

test_config = read_json(
    os.path.join(TEST_CONFIG_DATA_DIR, "default/unit/test-config_api.json")
)


class TestDataverse:
    @pytest.mark.v4_20
    @pytest.mark.parametrize(
        "test_input,expected", test_config["dataverse"]["valid"]["input-expected"]
    )
    def test_valid(self, config, native_api, test_input, expected):
        """Test important Dataverses."""
        # Arrange
        # Act
        resp = native_api.get_dataverse(test_input["alias"])
        r_data = resp.json()["data"]
        # Assert
        assert r_data["alias"] == expected["alias"]
        assert r_data["name"] == expected["name"]
        assert r_data["affiliation"] == expected["affiliation"]
        for c in r_data["dataverseContacts"]:
            assert c["contactEmail"] in expected["emails"]
        assert len(r_data["dataverseContacts"]) == len(expected["emails"])
        assert r_data["theme"]["tagline"] == expected["tagline"]
        assert r_data["theme"]["linkUrl"] == expected["link-url"]
        assert resp.status_code == 200
        assert resp.headers["Content-Type"] == "application/json"
        assert resp.url == expected["url"]
        # Cleanup
