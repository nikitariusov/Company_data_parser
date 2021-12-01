import requests


def get_response(url, headers, params=None):
    r = requests.get(url, headers=headers, params=params)
    return r


def get_html(response):
    if response.status_code == 200:
        return response.text

    else:
        print("[INFO] ERROR SERVER RESPONSE")
        return None
