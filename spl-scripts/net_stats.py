#!/usr/local/bin/python
# Script connects to the file that was created by splynx_stats.py and gets usage for selected period
# Run script this way: net_stats.py <network> - for example net_stats.py 2021-01-01 2021-02-01, it will show all usage per /24 range from the selected period
import splynx_stats as s
from sys import argv
import time
from tabulate import tabulate
import json
from datetime import date

start_time = time.time()

start_date = str(argv[1])
end_date = str(argv[2])
isp_usage = s.splynx_stats()

result = isp_usage.get_info(start_date, end_date)

#print(json.dumps(result,indent=2))
print(tabulate(result, headers='keys', tablefmt="grid"))


print("--- %s seconds ---" % (time.time() - start_time))

