# Run this file to connect to Splynx and save usage of all active customers to the file in /data/ folder

import splynx_api
import json
import os
from tabulate import tabulate

api_url = ''  # please set your Splynx URL
key = ""  # please set your key
secret = ""  # please set your secret

api = splynx_api.SplynxApi(api_url, key, secret)

class splynx_stats:
    def all_stats_to_file(self):

        ApiGetCustomers = "admin/customers/customer"

        api.api_call_get(ApiGetCustomers)
        customers_json = api.response
        a_customer_list = []

        for customer in customers_json:
            if customer['status'] == 'active' or customer['status'] == 'blocked':
                a_customer_list.append(customer['id'])

        directory = './data/'
        filename = str('all_stats.json')
        file_path = os.path.join(directory, filename)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        with open(file_path, 'w') as f:

            for id in a_customer_list:
                if a_customer_list.index(id) == 0:
                    f.write("[")

                ApiGetStats = "admin/customers/customer-statistics/" + id
                api.api_call_get(ApiGetStats)
                stats_json = api.response
                for session in stats_json:
                    data = {"session id": session['session_id'], "date": session['end_date'], "ip": session['ipv4'],
                            "download": session['in_bytes'], "upload": session['out_bytes']}
                    if a_customer_list.index(id) == -1:
                        f.write("]")
                    else:
                        f.write(str(data) + ",")

    def find_net(self, ip_address):
        ipaddress=ip_address
        ip = ip_address.split(".")
        net = [ip[0], ip[1], ip[2], "0"]
        net_address = ".".join(net)
        return (net_address)

    def get_info(self, start_date, end_date) :
        directory = './data/'
        filename = str('all_stats.json')
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r') as f:
            my_json = f.read()
        all_stats = json.loads(my_json)

        net_stats=[]
        net_list=[]
        for session in all_stats :
            if start_date < session["date"] and end_date > session["date"]:
                session["ip"] = self.find_net(session["ip"])
                net_stats.append(session)
                net_list.append(session["ip"])

        networks = (list(set(net_list)))    # this is the list of /24 networks
        networks.sort()

        final_stats=[]
        for net in networks :
            n_data = {"ip network" : net, "download" : 0, "upload" : 0}
            final_stats.append(n_data)

        for f in final_stats :
            for n in net_stats:
                if f["ip network"] == n["ip"] :
                    f["download"] = f["download"] + int(n["download"])
                    f["upload"]  = f["upload"] + int(n["upload"])

        view_stats = []
        for line in final_stats :
            data = {"IP network : " : (line["ip network"]+"/24"), "Download TB" : round((line["download"]/1000000000000),2), "Upload TB" : round((line["upload"]/1000000000000),2)}
            view_stats.append(data)

        return(view_stats)


#                print(self.find_net(session["ip_address"]))

#        print(self.find_net(all_stats[0]["ip"]))
#        print(self.find_net(all_stats[-1]["ip"]))


if __name__ == "__main__" :
    new_db = splynx_stats()
    new_db.all_stats_to_file()
