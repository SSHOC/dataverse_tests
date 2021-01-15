import os
from time import sleep

import pytest

from ..conftest import get_instance_dir, read_json, login_normal_user


class TestDataverses:
    def test_all_dataverses(self, config, test_config, firefox):
        if not test_config["tests"]["all-dataverses"]["test"]:
            pytest.skip("Test not configured to be executed.")

        instance_dir = get_instance_dir(config)
        base_url = test_config["instance"]["base-url"]
        dataverses = read_json(os.path.join(instance_dir, config.FILENAME_DATAVERSES))
        firefox = login_normal_user(
            firefox,
            test_config,
            config,
            config.USER_SUPERUSER,
            config.USER_SUPERUSER_PWD,
        )

        for dv in dataverses:
            url = f"{base_url}/dataverse.xhtml?alias={dv['dataverse_alias']}"
            firefox.get(url)
            sleep(1)
            assert url == firefox.current_url

            url = f"{base_url}/dataverse/{dv['dataverse_alias']}"
            firefox.get(url)
            sleep(1)
            assert url == firefox.current_url
