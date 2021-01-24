#!/usr/bin/env python
import json
from sys import argv
import os
import connect_ipregistry as con_reg
import iphelp
import time

start_time = time.time()

def display(ip_address, apiKey) :
    net_ip = iphelp.find_net(ip_address)
    try:
        directory = './cache/'
        filename = 'ipregistry_'+net_ip+'.json'
        file_path = os.path.join(directory, filename)

        with open(file_path, 'r') as f:
            ip_json=f.read()

        ip_addr = json.loads(ip_json)
#        print(json.dumps(ip_addr,indent=2))
        geo_info = {'database':'ipregistry.co', 'code': ip_addr["location"]["country"]["code"], 'country': ip_addr["location"]["country"]["name"], 'region' : ip_addr["location"]["region"]["name"],
                   'city': ip_addr["location"]["city"], 'company': '', 'isp': ip_addr["connection"]["organization"], 'latitude' : ip_addr["location"]["latitude"], 'longitude' : ip_addr["location"]["longitude"]}

        return (geo_info)

    except IOError:
        ip_addr = con_reg.connect_api(ip_address, apiKey)
        geo_info = {'database':'ipregistry.co', 'code': ip_addr["location"]["country"]["code"], 'country': ip_addr["location"]["country"]["name"], 'region' : ip_addr["location"]["region"]["name"],
                   'city': ip_addr["location"]["city"], 'company': '', 'isp': ip_addr["connection"]["organization"], 'latitude' : ip_addr["location"]["latitude"], 'longitude' : ip_addr["location"]["longitude"]}
#        print(json.dumps(ip_addr, indent=2))
        return (geo_info)

if __name__ == "__main__" :
    arg_ip = argv[1]
    apiKey= argv[2]
    my_ip = iphelp.ip_check(arg_ip)
    ip_addr = display(my_ip, apiKey)

    print(f'''IP address :  {my_ip}
Database : {ip_addr["database"]}
Code : {ip_addr["code"]}
Country :  {ip_addr["country"]}
Region : {ip_addr["region"]}
City : {ip_addr["city"]}
ISP: {ip_addr["isp"]}
Geolocation: {ip_addr["latitude"]}, {ip_addr["longitude"]}
    '''
    )


    print("--- %s seconds ---" % (time.time() - start_time))

#print(type(ip_json)) # will print str, the json that we are reading from the file
#print(type(my_ip))  # will print dict, parsed json to the pythin dict



#for i in my_ip["ip_address"]:
#    print(i)
#print(f'''IP address :  {my_ip["ip"+str(i)]["ip"]}
#Country :  {my_ip["ip"+str(i)]["location"]["country"]["name"]}
#Code : {my_ip["ip"+str(i)]["location"]["country"]["code"]}
#Region : {my_ip["ip"+str(i)]["location"]["region"]["name"]}
#City : {my_ip["ip"+str(i)]["location"]["city"]}
#Company: {my_ip["ip"+str(i)]["connection"]["organization"]}
#        '''
#    )

#print(json.dumps(my_ip,indent=2))