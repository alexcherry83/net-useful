from requests import get
import os
import json
import iphelp

def connect_api(ip_address, apiKey):
    net_ip = iphelp.find_net(ip_address)
    try:
        url = 'https://api.ipgeolocation.io/ipgeo/'
        params = dict(apiKey=apiKey, ip=ip_address, excludes='time_zone,currency')
        getInfo = get(url=url, params=params)
        ipInfo = getInfo.json()
#        print(json.dumps(ipInfo, indent=2))
        directory = './cache/'
        filename = str('ipgeolocation_'+net_ip + '.json')
        file_path = os.path.join(directory, filename)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        with open(file_path, 'w') as f:
            f.write(json.dumps(ipInfo, indent=2))
        return (ipInfo)

    except:
        print("Cannot connect to API")