import requests
import pytest
from ynd_creds import TOKEN
HEADERS = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth ' + TOKEN
        }
URL = 'https://cloud-api.yandex.net/v1/disk/resources'
DATA_CREATE = [
    ('/api/', 'OK'),
    (123, 'OK'),
    (None, 'Failure')
]


def create_folder(folder_name):
    params = {'path': folder_name}
    response = requests.put(url=URL, params=params, headers=HEADERS)
    if response.status_code == 201:
        return 'OK'
    else:
        return 'Failure'


def check_folder(folder_name):
    params = {'path': folder_name}
    response = requests.get(url=URL, params=params, headers=HEADERS)
    if response.status_code == 200:
        return 'OK'
    else:
        return 'Failure'


class TestCreate:
    def setup(self):
        print('Checking folder creation')

    @pytest.mark.parametrize('folder_name, result', DATA_CREATE)
    def test_creating(self, folder_name, result):
        assert create_folder(folder_name) == result
        assert check_folder(folder_name) == result

    def teardown(self):
        print('\nFinish')
