import sys
import requests
from PIL import Image
from io import BytesIO

URL = "https://api.github.com/emojis"


def fetch_icons():
    try:
        res = requests.get(URL)
        # throwing an error in case the status is incorrect:
        res.raise_for_status()
        print("Request's status:", res.status_code)
        icons_list = list(res.json().keys())
        return icons_list
    except requests.exceptions.RequestException as e:
        print("There was an error ಥ_ಥ\n", e)
        sys.exit()


def print_all_icons_names():
    icons = fetch_icons()
    if not icons:
        print("No icons available")
    else:
        for i in icons:
            print(i, end=", ")


def search_icons_by_keyword(key):
    icons = fetch_icons()
    if icons:
        # Put in the array all the icons that contain the keyword:
        icon_found = [icon for icon in icons if key.lower() in icon.lower()]
        if icon_found:
            print("I found an available icons for you")
            for i in icon_found:
                print(i, end=", ")
        else:
            print("No icons match the keyword.")
    else:
        print("No icons available")


def display_icon(icon_name):
    try:
        # I redid this because the fetch_icons() function returns a list of strings...
        response = requests.get(URL)
        response.raise_for_status()
        icons = response.json()
        if icon_name in icons:
            image_url = icons[icon_name]
            response = requests.get(image_url)
            # Reading the image data from the request:
            img = Image.open(BytesIO(response.content))
            img.show()
        else:
            print("Icon not found :( ")
    except requests.RequestException.request as e:
        print("There was an error: ", e)
