import requests
from colorama import Style, Fore


def get_response(url, headers, params=None):
    r = requests.get(url, headers=headers, params=params)
    #   print("[TEST] get_response(r): ", r.text)
    return r


def get_html(response):
    if response.status_code == 200:
        #   print("[TEST] get_html(response.text): ", response.text)
        return response.text

    else:
        print(Fore.RED + "[INFO] ERROR SERVER RESPONSE")
        print(Style.RESET_ALL)
        return None
