import requests
from bs4 import BeautifulSoup
import re


def dms2dec(dms_str):
    dms_str = re.sub(r'\s', '', dms_str)

    sign = -1 if re.search('[swSW]', dms_str) else 1

    numbers = [*filter(len, re.split('\D+', dms_str, maxsplit=4))]

    degree = numbers[0]
    minute = numbers[1] if len(numbers) >= 2 else '0'
    second = numbers[2] if len(numbers) >= 3 else '0'
    frac_seconds = numbers[3] if len(numbers) >= 4 else '0'

    second += "." + frac_seconds
    return sign * (int(degree) + float(minute) / 60 + float(second) / 3600)


def find_coordinates_by_location(location: str):
    url = f"https://en.wikipedia.org/wiki/{location}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    latitude_result = soup.find("span", {"class": "latitude"}).contents[0]
    converted_lat = dms2dec(latitude_result)
    longitude_result = soup.find("span", {"class": "longitude"}).contents[0]
    converted_lon = dms2dec(longitude_result)

    return converted_lat, converted_lon


coordinates = find_coordinates_by_location("zoara")
coordinates2 = find_coordinates_by_location("Abarim")
print(coordinates)
print(coordinates2)
