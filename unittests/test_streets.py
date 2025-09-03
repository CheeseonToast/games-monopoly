# Copyright Gary Roberson 2024

from main.classes.street.street import Property
import json
from typing import List


def streets_factory():
    with open("../resources/game_data.json", 'r') as f:
        data = json.load(f)
    try:
        streets: List[Property] = []
        if len(streets) == 0:
            i = 0
            for site_type in data['site_type']:
                if site_type in [1]:
                    street_gen = Property(site_type, i)
                    i += 1
                    streets.append(street_gen)
    except Exception as e:
        return e
    finally:
        return "pass"


def test_create_streets(benchmark):
    """
    create streets
    :param benchmark:
    :return:
    """
    result = benchmark(streets_factory)
    assert result is "pass"
