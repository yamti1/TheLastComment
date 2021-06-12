import requests
import json
from time import sleep

FACEBOOK_API_URL = "https://graph.facebook.com/{target}"
USER_TOKEN = "EAAEOuHUSdj0BAFVnpOZB4yWlgkX6dcMUMcCzRJZCGlRelhzD4bBTPf94MOA9eim4c8ZA95fpmiWcXfVN4F0LhDt0bjTehotiwYdbZCmEGKGGGXRi06t2y7I2atAZA3SvRdFjLig1RxQGJR1XHDCuZBCJLYDbddIaG0E6qAqeU3RlPY5OY2kFVqTLy2F3s4g858Ue14ZC9KzcAZDZD"


def get_last_commenter_id(post_id):
    return ""


def get_my_id(user_token):
    """
    Returns the user ID of the user associated with the given token.
    :param user_token: A string. The token of the user.
    :return: A string. The ID of the user.
    :raises: RuntimeError if something goes wrong.
    """

    try:
        response = requests.get(
            FACEBOOK_API_URL.format(target="me"),
            {"access_token": user_token}
        )

    except ConnectionError as e:
        msg = "Could not get user's ID because of {}".format(str(e))
        raise RuntimeError(msg)

    if response.status_code != requests.codes["OK"]:
        msg = "Could not get user's ID because of response code {}".format(response.status_code)
        raise RuntimeError(msg)

    json_response = json.loads(response.text)

    return json_response["id"]


def comment():
    pass


def main():
    while True:
        if get_last_commenter_id() != get_my_id(USER_TOKEN):
            try:
                comment()
            except:
                pass

        sleep(10000)
