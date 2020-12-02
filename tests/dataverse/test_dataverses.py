import os
from time import sleep
from ..conftest import read_json, get_instance_dir


class TestDataverses:
    def test_all_dataverses(self, config, test_config, firefox):
        if test_config["tests"]["all-dataverses"]["test"]:
            instance_dir = get_instance_dir(config)
            base_url = test_config["instance"]["base-url"]
            dataverses = read_json(
                os.path.join(instance_dir, config.FILENAME_DATAVERSES)
            )

            for dv in dataverses:
                url = f"{base_url}/dataverse.xhtml?alias={dv['dataverse_alias']}"
                firefox.get(url)
                sleep(1)
                assert dv["title"] in firefox.title
                assert url == firefox.current_url

                url = f"{base_url}/dataverse/{dv['dataverse_alias']}"
                firefox.get(url)
                sleep(1)
                assert dv["title"] in firefox.title
                assert url == firefox.current_url
