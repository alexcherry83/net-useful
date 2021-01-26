from sys import argv
import time
import geo_class as ip

start_time = time.time()
data = []
ip2location_apiKey = ""
ipregistry_apiKey = ""
ipgeolocation_apiKey = ""
abstractapi_apiKey = ""
ipdata_apiKey = ""
astroip_apiKey = ""

ip_address = argv[1]

ip2location = ip.geo_data(ip_address, 'ip2location', ip2location_apiKey)
ipgeolocation = ip.geo_data(ip_address, 'ipgeolocation', ipgeolocation_apiKey)
ipregistry = ip.geo_data(ip_address, 'ipregistry', ipregistry_apiKey)
abstractapi = ip.geo_data(ip_address, 'abstractapi', abstractapi_apiKey)
ipdata = ip.geo_data(ip_address, 'ipdata', ipdata_apiKey)
astroip = ip.geo_data(ip_address, 'astroip', astroip_apiKey)


data.append(ip2location.get_info())
data.append(ipgeolocation.get_info())
data.append(ipregistry.get_info())
data.append(abstractapi.get_info())
data.append(ipdata.get_info())
data.append(astroip.get_info())

for i in range(6):
    print(f'''
------ {data[i]["database"].capitalize()} ------
IP address :  {ip2location.ip_address}
Database : {data[i]["database"]}
Code : {data[i]["code"]}
Country :  {data[i]["country"]}
Region : {data[i]["region"]}
City : {data[i]["city"]}
ISP: {data[i]["isp"]}
Company: {data[i]["company"]}
Geolocation: {data[i]["latitude"]}, {data[i]["longitude"]}
'''

 )

print("--- %s seconds ---" % (time.time() - start_time))