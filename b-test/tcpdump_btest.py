import datetime
import json
from tabulate import tabulate
from operator import itemgetter
import tcp_btest as b_test
from sys import argv
import time

start_time = time.time()

file_name = argv[1]
with open(file_name, 'r') as f:
    tcp_dump = f.read().rstrip().split('\n')

t_rows=[]
for i in tcp_dump:
    data = i.split(",")
    t_rows.append(data)
#print(json.dumps(t_rows,indent=4))

#data = {'timestamp': str(datetime.datetime.utcfromtimestamp(ts)), 'src_ip': inet_to_str(ip.src),
#        'dst_ip': inet_to_str(ip.dst), 'src': inet_to_str(ip.src) + ":" + str(src_port),
#        'dst': inet_to_str(ip.dst) + ":" + str(dst_port), 'frame_size': len(eth),
#        'session': inet_to_str(ip.src) + ":" + str(src_port) + '-' + inet_to_str(ip.dst) + ":" + str(dst_port)}

data_list=[]
tcp_rows=[]
for a in t_rows:
    for item in a:
        if a.index(item) == 0:
            first_element = item.strip().split(' ')
            data  = {'timestamp': (first_element[0])}

        if a.index(item) == 2:
            element = item.strip().split(':')
            length = element[0].split(' ')
            ip_addresses = element[1].strip().split('>')
            if len(ip_addresses)>1:
                src = ip_addresses[0].strip()
                dst = ip_addresses[1].strip()
                ip_no_port1 = src.split('.')
                ip_no_port2 = dst.split('.')
                src_ip = '.'.join(ip_no_port1[:-1])
                dst_ip = '.'.join(ip_no_port2[:-1])

                data1 = {'src_ip': src_ip, 'dst_ip': dst_ip, 'src' : src, 'dst' : dst, 'frame_size': (int(length[1])), 'session': src + '<->' + dst}
                data.update(data1)
                data_list.append(data)

            else :
                data.clear()



#print(json.dumps(data_list, indent=2))

my_test = b_test.tcp_bandwidth_test(data_list)
my_test.get_tcp_stats()

print("--- %s seconds ---" % (time.time() - start_time))
