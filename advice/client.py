#!/usr/bin/env python3
"""
Name: advice
Description: Fetch some random advice from api.adviceslip.com.
License: MIT
Author: Kevin Morris <kevr@0cost.org>
"""
import sys
from http import HTTPStatus

import requests


def get_advice():
    response = requests.get("https://api.adviceslip.com/advice")
    if response.status_code != int(HTTPStatus.OK):
        print("error: received error status code '{response.status_code}'",
              file=sys.stderr)
        return None

    # { "slip": { "id": 123, "advice": "..." } }
    advice = response.json().get("slip").get("advice")
    return f'"{advice}"'


if __name__ == "__main__":
    advice = get_advice()
    print(advice)
