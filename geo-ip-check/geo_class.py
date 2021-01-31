import requests
import os
import json
from ipwhois import IPWhois

class geo_data:
    def __init__(self, ip_address, service, apiKey, cache):
        self.ip_address = ip_address
        self.apiKey = apiKey
        self.service = service
        self.cache=cache

    '''
    Method is ip_check() is used to validate the IP address
    '''
    def ip_check(self):
        ip_address = self.ip_address
        ip = ip_address.split(".")

        if (ip.__len__()) != 4:
            print("You haven't entered the valid IP address with a '.' notation")
            self.ip_address = input("Please enter a valid IP address : ")
            self.ip_check()
        else:
            try:
                for i in ip:
                    if (int(i) < 0) or (int(i) > 255):
                        self.ip_address = input("Please enter valid IP address : ")
                        self.ip_check()
                        break
            except:
                print("Sorry, IP address has 4 fields with values 0-255 separated by comma, ")
                self.ip_address = input("please enter a valid IP address : ")
                self.ip_check()
        return (ip_address)

    '''
    Method is find_net() is used to get the IP address of the /24 network, to use it then for caching purposes
    '''

    def find_net(self):
        ip = self.ip_address.split(".")
        net = [ip[0], ip[1], ip[2], "0"]
        net_address = ".".join(net)
        return (net_address)

    '''
    Method connect_api() connects to the REST API of the GEO IP database and also saves a json file to cache folder to allow access it later.
    The file is created for the whole /24 network
    '''

    def connect_api(self):
        self.ip_check()
        net_ip_address = self.find_net()

        if self.service == 'ip2location':
            self.url='https://api.ip2location.com/v2/'

        elif self.service == 'ipregistry':
            self.url = 'https://api.ipregistry.co/'+self.ip_address

        elif self.service == 'ipgeolocation':
            self.url = 'https://api.ipgeolocation.io/ipgeo/'

        elif self.service == 'abstractapi':
            self.url = 'https://ipgeolocation.abstractapi.com/v1/'

        elif self.service == 'ipdata':
            self.url = 'https://api.ipdata.co/'+self.ip_address

        elif self.service == 'astroip':
            self.url = 'https://api.astroip.co/'+self.ip_address

        try:
            url = self.url

            if self.service == 'ip2location':
                params = dict(key=self.apiKey, ip=self.ip_address, package='WS6', lang='en')

            elif self.service == 'ipgeolocation':
                params = dict(apiKey=self.apiKey, ip=self.ip_address, excludes='time_zone,currency')

            elif self.service == 'ipregistry':
                params = dict(key=self.apiKey)

            elif self.service == 'abstractapi':
                params = dict(api_key=self.apiKey, ip_address=self.ip_address)

            elif self.service == 'ipdata':
                params = {'api-key' : self.apiKey}

            elif self.service == 'astroip':
                params = dict(api_key=self.apiKey)

            getInfo = requests.get(url=url, params=params)
            ipInfo = getInfo.json()
            #        print(json.dumps(ipInfo, indent=2))
            directory = './cache/'
            filename = str(self.service + '_' + net_ip_address + '.json')
            file_path = os.path.join(directory, filename)
            if not os.path.isdir(directory):
                os.mkdir(directory)
            with open(file_path, 'w') as f:
                f.write(json.dumps(ipInfo, indent=2))
            return (ipInfo)

        except:
            print("Cannot connect to API")


    '''
    Method get_info() attempts to read the cache file first, if it doesn't exist, it calls connect_api() method and connects to REST API + saves the local cache file 
    and returns the dictionary with content of the GEO IP data
    '''

    def get_info(self) :
        self.ip_check()
        net_ip_address = self.find_net()

        if self.cache != 'nocache':
            try:
                directory = './cache/'
                filename = self.service + '_' + net_ip_address + '.json'
                file_path = os.path.join(directory, filename)

                with open(file_path, 'r') as f:
                    ip_json=f.read()

                ip_addr = json.loads(ip_json)

                if self.service == 'ip2location' :
                    geo_info = {'database':'ip2location.com',
                                'code': ip_addr["country_code"],
                                'country': ip_addr["country_name"],
                                'region' : ip_addr["region_name"],
                                'city': ip_addr["city_name"],
                                'company': '',
                                'isp': ip_addr["isp"],
                                'latitude' : ip_addr["latitude"],
                                'longitude' : ip_addr["longitude"]}

                elif self.service == 'ipgeolocation':
                    geo_info = {'database': 'ipgeolocation.io',
                                'code': ip_addr["country_code2"],
                                'country': ip_addr["country_name"],
                                'region': ip_addr["state_prov"],
                                'city': ip_addr["city"],
                                'company': ip_addr["organization"],
                                'isp': ip_addr["isp"],
                                'latitude': ip_addr["latitude"],
                                'longitude': ip_addr["longitude"]}

                elif self.service == 'ipregistry':
                    geo_info = {'database': 'ipregistry.co',
                                'code': ip_addr["location"]["country"]["code"],
                                'country': ip_addr["location"]["country"]["name"],
                                'region': ip_addr["location"]["region"]["name"],
                                'city': ip_addr["location"]["city"],
                                'company': '',
                                'isp': ip_addr["connection"]["organization"],
                                'latitude': ip_addr["location"]["latitude"],
                                'longitude': ip_addr["location"]["longitude"]}

                elif self.service == 'abstractapi':
                    geo_info = {'database': 'abstractapi.com',
                                'code': ip_addr["country_code"],
                                'country': ip_addr["country"],
                                'region': ip_addr["region"],
                                'city': ip_addr["city"],
                                'company': ip_addr["connection"]["organization_name"],
                                'isp': ip_addr["connection"]["isp_name"],
                                'latitude': ip_addr["latitude"],
                                'longitude': ip_addr["longitude"]}

                elif self.service == 'ipdata':
                    geo_info = {'database': 'ipdata.co',
                                'code': ip_addr["country_code"],
                                'country': ip_addr["country_name"],
                                'region': ip_addr["region"],
                                'city': ip_addr["city"],
                                'company': '',
                                'isp': ip_addr["asn"]["name"] if ("asn" in ip_addr) else '',
                                'latitude': ip_addr["latitude"] if ("latitude" in ip_addr) else '',
                                'longitude': ip_addr["longitude"] if ("longitude" in ip_addr) else ''
                                }

                elif self.service == 'astroip':
                    geo_info = {'database': 'astroip.co',
                                'code': ip_addr["geo"]["country_code"],
                                'country': ip_addr["geo"]["country_name"],
                                'region': ip_addr["geo"]["region_name"],
                                'city': ip_addr["geo"]["city"],
                                'company': ip_addr["asn"]["organization"] if (ip_addr["asn"] is not None) else '',
                                'isp': ip_addr["asn"]["asn"] if (ip_addr["asn"] is not None) else '',
                                'latitude': ip_addr["geo"]["latitude"],
                                'longitude': ip_addr["geo"]["longitude"]}


                return (geo_info)

            except IOError:
                ip_addr = self.connect_api()
                if self.service == 'ip2location':
                    geo_info = {'database': 'ip2location.com',
                                'code': ip_addr["country_code"],
                                'country': ip_addr["country_name"],
                                'region': ip_addr["region_name"],
                                'city': ip_addr["city_name"],
                                'company': '',
                                'isp': ip_addr["isp"],
                                'latitude': ip_addr["latitude"],
                                'longitude': ip_addr["longitude"]}

                elif self.service == 'ipgeolocation':
                    geo_info = {'database': 'ipgeolocation.io',
                                'code': ip_addr["country_code2"],
                                'country': ip_addr["country_name"],
                                'region': ip_addr["state_prov"],
                                'city': ip_addr["city"],
                                'company': ip_addr["organization"],
                                'isp': ip_addr["isp"],
                                'latitude': ip_addr["latitude"],
                                'longitude': ip_addr["longitude"]}

                elif self.service == 'ipregistry':
                    geo_info = {'database': 'ipregistry.co',
                                'code': ip_addr["location"]["country"]["code"],
                                'country': ip_addr["location"]["country"]["name"],
                                'region': ip_addr["location"]["region"]["name"],
                                'city': ip_addr["location"]["city"],
                                'company': '',
                                'isp': ip_addr["connection"]["organization"],
                                'latitude': ip_addr["location"]["latitude"],
                                'longitude': ip_addr["location"]["longitude"]}

                elif self.service == 'abstractapi':
                    geo_info = {'database': 'abstractapi.com',
                                'code': ip_addr["country_code"],
                                'country': ip_addr["country"],
                                'region': ip_addr["region"],
                                'city': ip_addr["city"],
                                'company': ip_addr["connection"]["organization_name"],
                                'isp': ip_addr["connection"]["isp_name"],
                                'latitude': ip_addr["latitude"],
                                'longitude': ip_addr["longitude"]}

                elif self.service == 'ipdata':
                    geo_info = {'database': 'ipdata.co',
                                'code': ip_addr["country_code"],
                                'country': ip_addr["country_name"],
                                'region': ip_addr["region"],
                                'city': ip_addr["city"],
                                'company': '',
                                'isp': ip_addr["asn"]["name"] if ("asn" in ip_addr) else '',
                                'latitude': ip_addr["latitude"] if ("latitude" in ip_addr) else '',
                                'longitude': ip_addr["longitude"] if ("longitude" in ip_addr) else ''}

                elif self.service == 'astroip':
                    geo_info = {'database': 'astroip.co',
                                'code': ip_addr["geo"]["country_code"],
                                'country': ip_addr["geo"]["country_name"],
                                'region': ip_addr["geo"]["region_name"],
                                'city': ip_addr["geo"]["city"],
                                'company': ip_addr["asn"]["organization"] if (ip_addr["asn"] is not None) else '',
                                'isp': ip_addr["asn"]["asn"] if (ip_addr["asn"] is not None) else '',
                                'latitude': ip_addr["geo"]["latitude"],
                                'longitude': ip_addr["geo"]["longitude"]}

                #        print(json.dumps(ip_addr, indent=2))

                return geo_info

        else:
            ip_addr = self.connect_api()
            if self.service == 'ip2location':
                geo_info = {'database': 'ip2location.com',
                            'code': ip_addr["country_code"],
                            'country': ip_addr["country_name"],
                            'region': ip_addr["region_name"],
                            'city': ip_addr["city_name"],
                            'company': '',
                            'isp': ip_addr["isp"],
                            'latitude': ip_addr["latitude"],
                            'longitude': ip_addr["longitude"]}

            elif self.service == 'ipgeolocation':
                geo_info = {'database': 'ipgeolocation.io',
                            'code': ip_addr["country_code2"],
                            'country': ip_addr["country_name"],
                            'region': ip_addr["state_prov"],
                            'city': ip_addr["city"],
                            'company': ip_addr["organization"],
                            'isp': ip_addr["isp"],
                            'latitude': ip_addr["latitude"],
                            'longitude': ip_addr["longitude"]}

            elif self.service == 'ipregistry':
                geo_info = {'database': 'ipregistry.co',
                            'code': ip_addr["location"]["country"]["code"],
                            'country': ip_addr["location"]["country"]["name"],
                            'region': ip_addr["location"]["region"]["name"],
                            'city': ip_addr["location"]["city"],
                            'company': '',
                            'isp': ip_addr["connection"]["organization"],
                            'latitude': ip_addr["location"]["latitude"],
                            'longitude': ip_addr["location"]["longitude"]}

            elif self.service == 'abstractapi':
                geo_info = {'database': 'abstractapi.com',
                            'code': ip_addr["country_code"],
                            'country': ip_addr["country"],
                            'region': ip_addr["region"],
                            'city': ip_addr["city"],
                            'company': ip_addr["connection"]["organization_name"],
                            'isp': ip_addr["connection"]["isp_name"],
                            'latitude': ip_addr["latitude"],
                            'longitude': ip_addr["longitude"]}

            elif self.service == 'ipdata':
                geo_info = {'database': 'ipdata.co',
                            'code': ip_addr["country_code"],
                            'country': ip_addr["country_name"],
                            'region': ip_addr["region"],
                            'city': ip_addr["city"],
                            'company': '',
                            'isp': ip_addr["asn"]["name"] if ("asn" in ip_addr) else '',
                            'latitude': ip_addr["latitude"] if ("latitude" in ip_addr) else '',
                            'longitude': ip_addr["longitude"] if ("longitude" in ip_addr) else ''}

            elif self.service == 'astroip':
                geo_info = {'database': 'astroip.co',
                            'code': ip_addr["geo"]["country_code"],
                            'country': ip_addr["geo"]["country_name"],
                            'region': ip_addr["geo"]["region_name"],
                            'city': ip_addr["geo"]["city"],
                            'company': ip_addr["asn"]["organization"] if (ip_addr["asn"] is not None) else '',
                            'isp': ip_addr["asn"]["asn"] if (ip_addr["asn"] is not None) else '',
                            'latitude': ip_addr["geo"]["latitude"],
                            'longitude': ip_addr["geo"]["longitude"]}

            #        print(json.dumps(ip_addr, indent=2))

            return geo_info

class rir_data:
    def __init__(self, ip_address):
        self.ip_address = ip_address
    def ip_check(self):
        ip_address = self.ip_address
        ip = ip_address.split(".")

        if (ip.__len__()) != 4:
            print("You haven't entered the valid IP address with a '.' notation")
            self.ip_address = input("Please enter a valid IP address : ")
            self.ip_check()
        else:
            try:
                for i in ip:
                    if (int(i) < 0) or (int(i) > 255):
                        self.ip_address = input("Please enter valid IP address : ")
                        self.ip_check()
                        break
            except:
                print("Sorry, IP address has 4 fields with values 0-255 separated by comma, ")
                self.ip_address = input("please enter a valid IP address : ")
                self.ip_check()
        return (ip_address)


    def get_info(self):
        self.ip_check()
        obj = IPWhois(self.ip_address)
        ip_rir = obj.lookup_rdap(depth=2)

        entities = ip_rir["entities"]
        #print(entities)
        org_name = ''
        for i in entities :
            if i[0:3] == "ORG":
                org_name = i

        rir_info = { 'network' : ip_rir["network"]["cidr"],
                    'parent_network' : ip_rir["network"]["parent_handle"],
                    'database': ip_rir["asn_registry"],
                    'network_name': ip_rir["network"]["name"],
                    'code': ip_rir["network"]["country"],
                    'type': ip_rir["network"]["type"],
                    'org': org_name if (org_name != '') else '',
                    'company': ip_rir["objects"][org_name]["contact"]["name"] if (org_name != '') else '',
                    'address': ip_rir["objects"][org_name]["contact"]["address"][0]["value"] if (org_name!='') else '',
                    'asn' : ip_rir["asn"],
                    'asn_country': ip_rir["asn_country_code"]
         }

        return rir_info

