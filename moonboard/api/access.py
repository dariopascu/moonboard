import os
import requests

ACCESS_ENDPOINT = "https://restapimoonboard.ems-x.com/token"

HEADERS = {
    'accept-encoding': 'gzip, gzip',
    'content-type': 'application/x-www-form-urlencoded',
    'host': 'restapimoonboard.ems-x.com',
    'user-agent': 'MoonBoard/1.0',
}


def get_access_token():
    data = {
        'refresh_token': __get_refresh_token(),
        'grant_type': 'refresh_token',
        'client_id': 'com.moonclimbing.mb'
    }
    r = requests.get(
        ACCESS_ENDPOINT,
        headers=HEADERS,
        data=data
    )
    return r.json()['access_token']


def __get_refresh_token():
    data = {
        'username': os.environ['MOONBOARD_USER'],
        'password': os.environ['MOONBOARD_PASSWORD'],
        'grant_type': 'password',
        'client_id': 'com.moonclimbing.mb',
    }
    r = requests.get(
        ACCESS_ENDPOINT,
        headers=HEADERS,
        data=data,
    )
    return r.json()['refresh_token']
