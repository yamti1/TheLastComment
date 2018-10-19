import requests
import json
from time import sleep

FACEBOOK_API_URL = "https://graph.facebook.com/{target}?access_token={access_token}"
USER_TOKEN = "EAAEOuHUSdj0BAFVnpOZB4yWlgkX6dcMUMcCzRJZCGlRelhzD4bBTPf94MOA9eim4c8ZA95fpmiWcXfVN4F0LhDt0bjTehotiwYdbZCmEGKGGGXRi06t2y7I2atAZA3SvRdFjLig1RxQGJR1XHDCuZBCJLYDbddIaG0E6qAqeU3RlPY5OY2kFVqTLy2F3s4g858Ue14ZC9KzcAZDZD"


def get_last_commenter_id():
    return ""


def get_my_id():
    return ""


def comment():
    pass


def main():
    while True:
        if get_last_commenter_id() != get_my_id():
            try:
                comment()
            except:
                pass

        sleep(10000)
