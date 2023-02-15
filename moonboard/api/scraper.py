import requests
from .access import get_access_token
from moonboard.config import Setup

BASE_URL = 'https://restapimoonboard.ems-x.com/v1/_moonapi/problems/v3/'
MAX_API_PROBLEM_PETITION = 5000


def get_json_data(
        initial_problem,
        moonboard_setup: Setup,
        json_data=None,

):
    url = f'{BASE_URL}{moonboard_setup.value[0]}/{moonboard_setup.value[1]}/{initial_problem}'

    headers = {
        'accept-encoding': 'gzip, gzip',
        'authorization': f'BEARER {get_access_token()}',
        'host': 'restapimoonboard.ems-x.com',
        'user-agent': 'MoonBoard/1.0',
    }

    if json_data is None:
        json_data = {}

    temp_json = requests.get(
        url,
        headers=headers
    ).json()
    if initial_problem == 0:
        json_data = requests.get(
            url,
            headers=headers
        ).json()
    else:
        for data in temp_json['data']:
            json_data['data'].append(data)

    if len(temp_json['data']) == MAX_API_PROBLEM_PETITION:
        return get_json_data(
            json_data['data'][-1]['apiId'],
            moonboard_setup,
            json_data,
        )
    else:
        return json_data
