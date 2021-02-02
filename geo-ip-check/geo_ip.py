from sys import argv
import time
import geo_class as ip
import geoip2.webservice

start_time = time.time()
data = []
ip2location_apiKey = ""
ipregistry_apiKey = ""
ipgeolocation_apiKey = ""
abstractapi_apiKey = ""
ipdata_apiKey = ""
astroip_apiKey = ""
#XXXX below is the user account on maxmind webservice
maxmind_user = XXXXX 
maxmind_code = ""

ip_argv = argv[1]
cache = 'yes'
try :
    cache = argv[2]
except:
    pass

ip_object = ip.parent_data(ip_argv)
ip_address = ip_object.ip_check()

rir_location = ip.rir_data(ip_address)
rir_data = rir_location.get_info()

maxmind = ip.maxmind_data(ip_address, maxmind_user, maxmind_code)
ip2location = ip.geo_data(ip_address, 'ip2location', ip2location_apiKey, cache)
ipgeolocation = ip.geo_data(ip_address, 'ipgeolocation', ipgeolocation_apiKey, cache)
ipregistry = ip.geo_data(ip_address, 'ipregistry', ipregistry_apiKey, cache)
abstractapi = ip.geo_data(ip_address, 'abstractapi', abstractapi_apiKey, cache)
ipdata = ip.geo_data(ip_address, 'ipdata', ipdata_apiKey, cache)
astroip = ip.geo_data(ip_address, 'astroip', astroip_apiKey, cache)

data.append(maxmind.get_info())
data.append(ip2location.get_info())
data.append(ipgeolocation.get_info())
data.append(ipregistry.get_info())
data.append(abstractapi.get_info())
data.append(ipdata.get_info())
data.append(astroip.get_info())


print(f'''
------ {rir_data["database"].upper()} ------
IP address :  {rir_location.ip_address}
Network :  {rir_data["network"]}
Type: {rir_data["type"]}
Parent network : {rir_data["parent_network"]}
Country code : {rir_data["code"]}
Org object :  {rir_data["org"]}
Company : {rir_data["company"]}
Address : {rir_data["address"]}
ASN : AS{rir_data["asn"]}
ASN Country : {rir_data["asn_country"]}
Last updated : {rir_data["updated"]}
'''
)


for i in range(7):
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
