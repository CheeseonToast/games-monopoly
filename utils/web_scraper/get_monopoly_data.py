# Copyright Gary Roberson 2024

from io import StringIO

import requests
import pandas as pd
import os

url = "https://en.wikibooks.org/wiki/Monopoly/Properties_reference"
html = requests.get(url).text
file_path = os.path.abspath("../../resources/property_data.json")
datafile = pd.read_html(StringIO(html))[-1].to_json(file_path)
