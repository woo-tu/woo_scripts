#! /usr/bin/python3


import random

import pyperclip
import requests

from random_usernames import random_words_ls


selection = []

while len(selection) < 2:
    new_selection = random_words_ls[random.randint(
        0, len(random_words_ls) - 1)]
    if new_selection not in selection and len(new_selection) < 5:
        selection.append(new_selection.title())
    else:
        pass


new_username = "".join(selection)
while len(new_username) < 11:
    new_username += str(random.randint(0, 9))
print(new_username)
pyperclip.copy(new_username)

r = requests.get("https://coreyms.com")
print(r.status_code)
