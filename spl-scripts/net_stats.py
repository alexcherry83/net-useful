#!/usr/bin/env python3
# Run script this way: net_stats.py <network> - for example net_stats.py 10.0.0.0/20

import splynx_api
import json
import codecs
from sys import argv
import split_net

#Get all sessions for selected period
#Aggregate them all to /24 prefixes
#Provide usage of /24 network for selected period

api_url = '' # please set your Splynx URL
key = "" # please set your key
secret = "" # please set your secret

ApiUrlNet = "admin/customers/customer-statistics" #API customers URL
api = splynx_api.SplynxApi(api_url, key, secret) 
api.api_call_get(ApiUrlNet)

json_network = api.response

#print(json.dumps(json_network, sort_keys=True, indent=4))

sessions = []
for i in range(7):
    sessions.append([])
    
my_id=0    
for ses in json_network:
	sessions[0].append(ses['session_id'])
	sessions[1].append(ses['ipv4'])
	sessions[2].append(ses['in_bytes'])
	sessions[3].append(ses['out_bytes'])
	sessions[4].append(ses['start_date'])
	sessions[5].append(ses['end_date'])
	sessions[6].append(str(my_id))
	my_id+=1
	
total=0
for a in range(len(sessions[2])):
	total=total+int(sessions[2][a])+int(sessions[3][a])
	
in_total=0
for a1 in range(len(sessions[2])):
	in_total=in_total+int(sessions[2][a1])

out_total=0
for a2 in range(len(sessions[2])):
	out_total=out_total+int(sessions[3][a2])
	
	
net_lst=[]  
for i1 in range(5):
    net_lst.append([])	


for id in range(len(sessions[1])):
	lst = sessions[1][id].split('.')
	net_lst[0].append(lst[0])
	net_lst[1].append(lst[1])
	net_lst[2].append(lst[2])
	net_lst[3].append(lst[3])
	net_lst[4].append(sessions[6][id])    
   

ip_range = argv[1:]
networks = split_net.c_class(ip_range)
networks.append([])
networks.append([])

for fill in range(len(networks[0])):
	networks[4].append(0)
	networks[5].append(0)
#	print(str(networks[0][nt]) + '.' + str(networks[1][nt]) + '.' + str(networks[2][nt]) + '.' + str(networks[3][nt]) + '/24')

#print(type(net_lst[4][0]))

id=0
nt=0

for nt in range(len(networks[0])):
	for id in range(len(net_lst[4])):
		if int(net_lst[0][id]) == networks[0][nt] and int(net_lst[1][id]) == networks[1][nt] and int(net_lst[2][id]) == networks[2][nt]:
			index = int(net_lst[4][id])
			networks[4][nt] = networks[4][nt] + int(sessions[2][index])
			networks[5][nt] = networks[5][nt] + int(sessions[3][index])
	

bit=0
print('Usage for networks:')
for bit in range(len(networks[0])):

	print(str(networks[0][bit]) + '.' + str(networks[1][bit]) + '.' + str(networks[2][bit]) + '.' + str(networks[3][bit]) + '/24   Download :' + str(round(networks[4][bit]/1000000,2)) + ' MB   Uplolad: ' + str(round(networks[5][bit]/1000000,2)) + ' MB   Total: ' + str(round((networks[4][bit]+networks[5][bit])/1000000,2)) + ' MB')	
	
	
