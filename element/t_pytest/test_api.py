import pytest
import requests
from yamlutil import YamlUtil


class TestApi:
    @pytest.mark.parametrize("args", YamlUtil('./test.yaml').read_yaml())
    def test_01_baidu(self, args):
        print(args)
        url = args['request']['url']
        params = args['request']['params']
        print(f'{url}\n{params}')
        http_code = requests.get(url, params=params).status_code
        assert http_code == 200
