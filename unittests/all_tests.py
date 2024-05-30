import os
from datetime import datetime


date_time_format = "%Y%m%d_%H"
name = "monopoly"
time_stamp = datetime.now().strftime(date_time_format)

os.system(f'pytest -rP --benchmark-histogram=.benchmarks/{name}_{time_stamp} --benchmark-timer=time.perf_counter')
