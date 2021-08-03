import random

import requests

import globals


def select_color_codes():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    if (r, g, b) not in globals.color_codes:
        globals.color_codes.append((r, g, b, 150))  # transparency (alpha=150)
        if len(globals.color_codes) > 5:
            globals.color_codes = globals.color_codes[1:]
        return r, g, b

    return select_color_codes()


def ping_address(web_address):
    """
    find if a particular address is valid or not
    :param web_address:
    :return:
    """
    ret_val = -1
    try:
        page = requests.get(web_address, timeout=globals.timeout)
        if page.status_code == 200:
            ret_val = 1
    except Exception as e:
        pass
    finally:
        return ret_val
