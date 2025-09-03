# Copyright Gary Roberson 2024

from main.classes.site.sites import Property
import json
from typing import List


def sites_factory():
	with open("../resources/game_data.json", 'r') as f:
		data = json.load(f)
	try:
		sites: List[Property] = []
		if len(sites) == 0:
			i = 0
			for site_type in data['site_type']:
				if site_type in [1]:
					site_gen = Property(site_type, i)
					i += 1
					sites.append(site_gen)
	except Exception as e:
		return e
	finally:
		return "pass"


def test_create_sites(benchmark):
	"""
	create sites
	:param benchmark:
	:return:
	"""
	result = benchmark(sites_factory)
	assert result == "pass"
