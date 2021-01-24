#!/usr/bin/env python

from ipregistry import ApiError, ClientError, IpregistryClient
import os
import json
import iphelp

def connect_api(ip_address, apiKey):
    net_ip = iphelp.find_net(ip_address)
    try:
        client = IpregistryClient(apiKey)
        ipInfo = client.lookup(ip_address)
#        with open(str(ipInfo["ip"])+'.json', 'w') as f :    - simple way, save to same directory
        directory = './cache/'
        filename = str('ipregistry_'+ net_ip + '.json')
        file_path = os.path.join(directory, filename)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        with open(file_path, 'w') as f:
            f.write(json.dumps(ipInfo, indent=2))
        return (ipInfo)
#    print(f'''IP address :  {ipInfo["ip"]}
#Country :  {ipInfo["location"]["country"]["name"]}
#Code : {ipInfo["location"]["country"]["code"]}
#Region : {ipInfo["location"]["region"]["name"]}
#City : {ipInfo["location"]["city"]}
#Company: {ipInfo["connection"]["organization"]}
#         '''
#    )

#    with open('geoisp.json', 'w') as f:
#        f.write(json.dumps(ipInfo))

#    with open('geoisp.json') as f:
#        print(f.read())

    except ApiError as e:
        print("API error", e)
    except ClientError as e:
        print("Client error", e)
    except Exception as e:
        print("Unexpected error", e)

#connect(my_ip)