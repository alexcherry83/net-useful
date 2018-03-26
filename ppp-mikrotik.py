#!/usr/bin/env python
# -*- coding: utf-8 -*-
import splynx_api
import json
import codecs

# set API variables

api_url = '' # please set your Splynx URL
key = "" # please set your key
secret = "" # please set your secret


# Let's get all customers IDs from Splynx 
ApiUrlCust = "admin/customers/customer" #API customers URL
api = splynx_api.SplynxApi(api_url, key, secret) 
api.api_call_get(ApiUrlCust)

json_object = api.response

# OK, customers are in JSON object now, we need to get all their IDs :

cust_id_list = []
for cust in json_object:
    cust_id_list.append(cust['id'])


# Got IDs of all customers from DB, need to grab all active Internet services from Splynx

ppp_array = []
for i in range(8):
    ppp_array.append([])

for id in cust_id_list:
    ApiServ = "admin/customers/customer/" + id + "/internet-services"
    api.api_call_get(ApiServ)
    json_service = api.response
    
    for cust_serv in json_service:
        if cust_serv['status'] == 'active':
            ppp_array[0].append(cust_serv['login'])
            ppp_array[1].append(cust_serv['password'])
            ppp_array[2].append(cust_serv['ipv4'])
            ppp_array[3].append(cust_serv['tariff_id'])
            ppp_array[4].append(0)
            ppp_array[5].append(0)
            ppp_array[6].append(cust_serv['customer_id'])
            ppp_array[7].append(0)
            print("Got service for customer ID " + cust_serv['customer_id'])
            

# Get the speeds from tariff table Splynx and store in list "plan"

ApiPlan = "admin/tariffs/internet"
api.api_call_get(ApiPlan)
json_plan = api.response


count = 0
for x in ppp_array[3]:
    
    for plan in json_plan:
        if x==plan['id']:
#            print(ppp_array[4][count] + " Download: " + plan['speed_download'] + ", Upload: " + plan['speed_upload'])        
            ppp_array[4][count] = plan['speed_download']
            ppp_array[5][count] = plan['speed_upload']
            
    count = count + 1 
    


# Add Customer name to array + Customer password if service password is empty

customer = []
for i in range(3):
    customer.append([])

for id in cust_id_list:
    ApiServ = "admin/customers/customer/" + id
    api.api_call_get(ApiServ)
    json_customer = api.response
    customer[0].append(json_customer['id'])
    customer[1].append(json_customer['password'])
    customer[2].append(json_customer['name'])
    print("Got customer, ID " + json_customer['id'])

for i in range(len(ppp_array[6])):
    for x in range(len(customer[0])):
        if customer[0][x] == ppp_array[6][i]:
            ppp_array[7][i] = customer[2][x]
            
        if customer[0][x] == ppp_array[6][i] and len(ppp_array[1][i]) == 0 :
            ppp_array[1][i] = customer[1][x]
        

# Create file PPP Secrets for Mikrotik router

f_secrets = codecs.open('ppp_secret.rsc', 'w', encoding='utf-8') 
f_profile = codecs.open('ppp_profile.rsc', 'w', encoding='utf-8')

for i in range(len(ppp_array[0])):
    if len(ppp_array[2][i]) != 0:
        f_secrets.write ('ppp secret add name="' + ppp_array[0][i] + '" password=' + ppp_array[1][i] + " remote-address="  + ppp_array[2][i] + " profile=Splynx_" + ppp_array[3][i] + ' comment="' + ppp_array[7][i] + '"\n')
    else:
        f_secrets.write ('ppp secret add name="' + ppp_array[0][i] + '" password=' + ppp_array[1][i] + " profile=Splynx_" + ppp_array[3][i] + ' comment="' + ppp_array[7][i] + '"\n')
f_secrets.close()


# Create file PPP Profile for Mikrotik router

for plan in json_plan:
    f_profile.write ("/ppp profile add local-address=10.0.0.1 name=Splynx_" + plan['id'] + " rate-limit=" + plan['speed_download'] + "k/" + plan['speed_upload'] +"k \n")
f_profile.close()    
    

